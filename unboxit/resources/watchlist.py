from flask import Response, request
from flask.json import jsonify
from unboxit.models.models import User, WatchList
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import DoesNotExist, NotUniqueError
from unboxit.resources.errors import InternalServerError, MovieNotExistsError, MovieAlreadyExistsError

class WatchListApi(Resource):

    @jwt_required()
    def post(self):
        #try:
            user_id = get_jwt_identity()
            body = request.get_json()
            user = User.objects.get(id=user_id)
            watch_list = WatchList.objects.get(user_id=user_id)
            watch_list.update(push__imdb=body["imdb_id"])
            watch_list.save()
            return {'movie id': "str(id)"}, 200
        # except DoesNotExist:
        #     raise MovieNotExistsError
        # except NotUniqueError:
        #     raise MovieAlreadyExistsError