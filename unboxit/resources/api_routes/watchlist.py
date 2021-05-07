
from flask import request, make_response, jsonify
from flask.helpers import url_for
from werkzeug.utils import redirect
from unboxit.models.models import Watchlist, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import DoesNotExist, NotUniqueError, \
    ValidationError, FieldDoesNotExist
from unboxit.resources.utils.errors import EntryAlreadyExistsError, \
    SchemaValidationError, EntryNotExistsError
from unboxit.resources.utils.cache import cache
from unboxit.resources.utils.jwt import jwt
import json


class WatchlistsApi(Resource):
    """
        Make this a Resource by extending Flask Restfull Resource class,
        then this resource be executed when the methods
        it has match a HTTP request method.
    """
    @jwt_required(locations=['headers', 'cookies'])
    def get(self):
        """
            GET all watchlists documents and protect route.
        """
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
        """
            Insert a watchlist and protect route.
        """
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
            response = {
                "message": "Movie was added successfully.",
                "status": 200
            }
            return response
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise EntryAlreadyExistsError

    def add_to_cache(watchlist):
        """
            When a movie or show is added cache them
            to minimize requests to db.
        """
        watchlist_cache = cache.get('watchlist_cache')
        recommend = cache.get('recommend')
        add_to_cache = json.loads(watchlist.to_json())
        data = {"id": add_to_cache["imdb_id"],
                "type": add_to_cache["media_type"]}

        if watchlist_cache is None:
            watchlist_cache = []
            cache.set('watchlist_cache', watchlist_cache)

        if recommend is None:
            recommend = []
            cache.set('recommend', watchlist_cache)

        if add_to_cache not in watchlist_cache:
            watchlist_cache.append(add_to_cache)
            cache.set('watchlist_cache', watchlist_cache)

        if data not in recommend:
            recommend.append(data.copy())
            cache.set('recommend', recommend)


class WatchlistApi(Resource):
    """
        Make this a Resource by extending Flask Restfull Resource class,
        then this resource be executed when the methods
        t has match a HTTP request method.
    """
    @jwt_required(locations=['headers', 'cookies'])
    def delete(self, id):
        """
            DELETE method for one single document by ID.
        """
        try:
            identity = get_jwt_identity()
            watchlist = Watchlist.objects.get(
                id=id, added_by=identity['user_id'])
            watchlist.delete()
            WatchlistApi.delete_from_cache(id)
            response = {
                "message": "Movie was deleted successfully.",
                "status": 200
            }
            return jsonify(response)
        except (DoesNotExist, ValidationError):
            raise EntryNotExistsError

    def delete_from_cache(id):
        """
            If DELETE request is performed successfully
            make sure to delete from cache.
        """
        watchlist_cache = cache.get('watchlist_cache')
        recommend = cache.get('recommend')
        if id and watchlist_cache is not None and recommend is not None:
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

    @jwt_required(locations=['headers', 'cookies'])
    def get(self, id):
        """
            GET one single watchlist.
        """
        try:
            watchlist = Watchlist.objects.get(id=id).to_json()
            return make_response(watchlist, 200)
        except (DoesNotExist, ValidationError):
            raise EntryNotExistsError

    @jwt_required(locations=['headers', 'cookies'])
    def put(self, id):
        """
            Perform PUT request for adding and editing review,
            when done update cache.
        """
        try:
            body = request.get_json()
            Watchlist.objects.get(id=id).update(**body)
            watchlist = Watchlist.objects.get(id=id)
            WatchlistApi.update_to_cache(watchlist, id)
            response = {
                "message": "Entry was edited successfully.",
                "status": 200
            }
            return make_response(jsonify(response), 200)
        except (DoesNotExist, ValidationError):
            raise EntryNotExistsError

    def update_to_cache(watchlist, id):
        """
            Update cache upon updating database.
        """
        watchlist_cache = cache.get('watchlist_cache')
        if watchlist_cache is not None:
            updated_watchlist = json.loads(watchlist.to_json())
            for i in range(len(watchlist_cache)):
                if watchlist_cache[i]['_id']['$oid'] == id:
                    watchlist_cache[i] = updated_watchlist
            cache.set('watchlist_cache', watchlist_cache)
