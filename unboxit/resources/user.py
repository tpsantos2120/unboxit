import datetime
from flask import Response, request
from flask_jwt_extended import create_access_token
from unboxit.models.models import User, WatchList
from flask_restful import Resource


class RegisterUserApi(Resource):
    def post(self):
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        watchlist = WatchList(user_id=str(user.id))
        watchlist.save()
        id = user.id
        return {'id': str(id)}, 200


class LoginUserApi(Resource):
    def post(self):
        body = request.get_json()
        user = User.objects.get(username=body.get('username'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'response': "Access Denied"}, 403
        expires = datetime.timedelta(days=7)
        access_token = create_access_token(
            identity=str(user.id), expires_delta=expires)
        return {
            "response": "Logged in successfully",
            'token': access_token
        }, 200
