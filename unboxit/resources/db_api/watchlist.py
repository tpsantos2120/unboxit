
from flask import request, make_response, jsonify
from unboxit.models.models import Watchlist, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import DoesNotExist, NotUniqueError, ValidationError, FieldDoesNotExist
from unboxit.resources.utils.errors import EntryAlreadyExistsError, SchemaValidationError, EntryNotExistsError
from unboxit.resources.utils.cache import cache
import json


class WatchlistsApi(Resource):
    @jwt_required(locations=['headers', 'cookies'])
    def get(self):
        try:
            identity = get_jwt_identity()
            watchlists = []
            if identity:
                user = User.objects.get(id=identity['user_id'])
                if user.watchlists and not len(user.watchlists) == 0:
                    for watchlist in user.watchlists:
                        watch_list = Watchlist.objects.get(id=watchlist.id)
                        watchlists.append(watch_list)
                return jsonify(watchlists)
        except DoesNotExist:
            raise EntryNotExistsError


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
        recommend = cache.get('recommend')
        add_to_cache = json.loads(watchlist.to_json())
        data = {"id": add_to_cache["imdb_id"],
                "type": add_to_cache["media_type"]}

        if watchlist_cache == None:
            watchlist_cache = []
            cache.set('watchlist_cache', watchlist_cache)

        if recommend == None:
            recommend = []
            cache.set('recommend', watchlist_cache)

        if not add_to_cache in watchlist_cache:
            watchlist_cache.append(add_to_cache)
            cache.set('watchlist_cache', watchlist_cache)

        if not data in recommend:
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
        return jsonify(response)

    def delete_from_cache(id):
        watchlist_cache = cache.get('watchlist_cache')
        recommend = cache.get('recommend')
        print("before", recommend)
        if id and not watchlist_cache == None and not recommend == None:
            for watchlist in watchlist_cache:
                if watchlist['_id']['$oid'] == id:
                    print(watchlist['_id']['$oid'], id)
                    watchlist_cache.remove(watchlist)
                    cache.set('watchlist_cache', watchlist_cache)
                    data = {"id": watchlist['imdb_id'],
                            "type": watchlist['media_type']}
                    if data in recommend:
                        recommend.remove(data)
                        cache.set('recommend', recommend)
        print("after", recommend)



    @jwt_required(locations=['headers', 'cookies'])
    def get(self, id):
        watchlist = Watchlist.objects.get(id=id).to_json()
        return make_response(watchlist, 200)


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
        return jsonify(response)


    def update_to_cache(watchlist, id):
        watchlist_cache = cache.get('watchlist_cache')
        if not watchlist_cache == None:
            updated_watchlist = json.loads(watchlist.to_json())
            print(updated_watchlist)
            for i in range(len(watchlist_cache)):
                if watchlist_cache[i]['_id']['$oid'] == id:
                    watchlist_cache[i] = updated_watchlist
            cache.set('watchlist_cache', watchlist_cache)
