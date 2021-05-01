
from flask import Response, request
from unboxit.models.models import Watchlist, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from bson import json_util
from mongoengine.errors import NotUniqueError, ValidationError, FieldDoesNotExist
from unboxit.resources.errors import InternalServerError, EntryAlreadyExistsError, SchemaValidationError
from .cache import cache
import json


class WatchlistsApi(Resource):
    @jwt_required(locations=['headers', 'cookies'])
    def get(self):
        identity = get_jwt_identity()
        watchlists = []
        if identity:
            user = User.objects.get(id=identity['user_id'])
            print(user.watchlists)
            if user.watchlists:
                for watchlist in user.watchlists:
                    watchlist = Watchlist.objects.get(id=watchlist.id).to_json()
                    watchlists.append(watchlist)
            return watchlists

    @jwt_required(locations=['headers', 'cookies'])
    def post(self):
        try:
            identity = get_jwt_identity()
            body = request.get_json()
            body["review"] = ""
            user = User.objects.get(id=identity['user_id'])
            watchlist = Watchlist(**body, added_by=user)
            watchlist.save()
            user.update(add_to_set__watchlists=watchlist)
            user.save()
            WatchlistsApi.add_to_cache(watchlist)
            response = {"ServerResponse": {
                "message": "Movie was added successfully.",
                "status": 200
            }}
            return response
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise EntryAlreadyExistsError

    def add_to_cache(watchlist):
        watchlist_cache = cache.get('watchlist_cache')
        print(watchlist_cache)
        add_to_cache = json.loads(watchlist.to_json())
        watchlist_cache.append(add_to_cache)
        print(watchlist_cache)
        cache.set('watchlist_cache', watchlist_cache)
        recommend = cache.get('recommend')
        data = {"id": add_to_cache["imdb_id"],
                    "type": add_to_cache["media_type"]}
        recommend.append(data.copy())
        cache.set('recommend', recommend)


class WatchlistApi(Resource):
    @jwt_required(locations=['headers', 'cookies'])
    def delete(self, id):
        identity = get_jwt_identity()
        watchlist = Watchlist.objects.get(id=id, added_by=identity['user_id'])
        watchlist.delete()
        WatchlistApi.delete_from_cache(id)
        response = {
            "message": "Movie was deleted successfully.",
            "status": 200
        }
        return response

    def delete_from_cache(id):
        if not cache.get('watchlist_cache') == None:
            watchlist_cache = cache.get('watchlist_cache')
            for watchlist in watchlist_cache:
                if watchlist['_id']['$oid'] == id:
                    watchlist_cache.remove(watchlist)
                    cache.set('watchlist_cache', watchlist_cache)
                    recommend = cache.get('recommend')
                    recommend.remove({"id": watchlist['imdb_id'],
                                      "type": watchlist['media_type']})
                    cache.set('recommend', recommend)

    @jwt_required(locations=['headers', 'cookies'])
    def get(self, id):
        watchlist = Watchlist.objects.get(id=id).to_json()
        return Response(watchlist, mimetype="application/json", status=200)

    @jwt_required(locations=['headers', 'cookies'])
    def put(self, id):
        body = request.get_json()
        print(body)
        Watchlist.objects.get(id=id).update(**body)
        watchlist = Watchlist.objects.get(id=id)
        WatchlistApi.update_to_cache(watchlist, id)
        response = {
            "message": "Movie was edited successfully.",
            "status": 200
        }
        return response

    def update_to_cache(watchlist, id):
        if not cache.get('watchlist_cache') == None:
            watchlist_cache = cache.get('watchlist_cache')
            updated_watchlist = json.loads(watchlist.to_json())
            for i in range(len(watchlist_cache)):
                if watchlist_cache[i]['_id']['$oid'] == id:
                    watchlist_cache[i] = updated_watchlist
            cache.set('watchlist_cache', watchlist_cache)
