import datetime
from flask import Response, request
from flask.helpers import make_response
from flask_jwt_extended import create_access_token
from flask_jwt_extended.utils import get_jwt_identity, set_access_cookies
from flask_jwt_extended.view_decorators import jwt_required
from unboxit.models.models import User
from flask_restful import Resource
from mongoengine.errors import DoesNotExist, FieldDoesNotExist, NotUniqueError
from unboxit.resources.errors import InternalServerError, UnauthorizedError, SchemaValidationError, EmailAlreadyExistsError


class RegisterUserApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = User(**body)
            user.hash_password()
            user.save()
            expires = datetime.timedelta(days=30)
            user_details = {
                "user_id": str(user.id),
                "first_name": user.first_name,
                "last_name": user.last_name
            }
            access_token = create_access_token(
                identity=user_details, expires_delta=expires)
            res = make_response({
                "response": "User registered successfully.",
                'token': access_token,
                "status": 200
            }, 200)
            set_access_cookies(res, access_token)
            return res
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception as e:
            raise InternalServerError


class LoginUserApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = User.objects.get(email=body.get('email'))
            authorized = user.check_password(body.get('password'))
            if not authorized:
                raise UnauthorizedError
            expires = datetime.timedelta(days=30)
            user_details = {
                "user_id": str(user.id),
                "first_name": user.first_name,
                "last_name": user.last_name
            }
            access_token = create_access_token(
                identity=user_details, expires_delta=expires)
            res = make_response({
                "response": "You have logged in successfully.",
                'status': 200
            }, 200)
            set_access_cookies(res, access_token)
            return res
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError

class ResetPassword(Resource):
    @jwt_required(locations=['headers', 'cookies'])
    def put(self):
        try:
            identity = get_jwt_identity()
            body = request.get_json()
            if identity:
                user = User.objects.get(id=identity['user_id'])
                user.modify(password=body.get('password'))
                user.hash_password()
                user.save()
            res = make_response({
                "response": "You have changed your password successfully.",
                'status': 200
            }, 200)
            return res
        except SchemaValidationError:
            raise SchemaValidationError
        except Exception as e:
            raise 