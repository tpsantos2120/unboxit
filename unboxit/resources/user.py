import datetime
from flask import Response, request
from flask_jwt_extended import create_access_token
from unboxit.models.models import User
from flask_restful import Resource
from mongoengine.errors import DoesNotExist
from unboxit.resources.errors import InternalServerError,UnauthorizedError


class RegisterUserApi(Resource):
    def post(self):
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        id = user.id
        return {'id': str(id)}, 200


class LoginUserApi(Resource):
    def post(self):
        try:
            body = request.form
            user = User.objects.get(email=body.get('email'))
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
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError
