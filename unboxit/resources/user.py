import datetime
from flask import Response, request
from flask_jwt_extended import create_access_token
from unboxit.models.models import User
from flask_restful import Resource
from mongoengine.errors import DoesNotExist, FieldDoesNotExist, NotUniqueError
from unboxit.resources.errors import InternalServerError, UnauthorizedError \
 , SchemaValidationError, EmailAlreadyExistsError


class RegisterUserApi(Resource):
    def post(self):
        try:
            body = request.form
            print(body.get('email'))
            user = User(**body)
            user.hash_password()
            user.save()
            expires = datetime.timedelta(days=7)
            access_token = create_access_token(
                identity=str(user.id), expires_delta=expires)
            return {
                "response": "User registered successfully.",
                'token': access_token
            }, 200
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception as e:
            raise InternalServerError


class LoginUserApi(Resource):
    def post(self):
        try:
            body = request.form
            print("login api",body)
            user = User.objects.get(email=body.get('email'))
            authorized = user.check_password(body.get('password'))
            if not authorized:
                return {'response': "Access Denied"}, 403
            expires = datetime.timedelta(days=7)
            access_token = create_access_token(
                identity=str(user.id), expires_delta=expires)
            return {
                "response": "Logged in successfully.",
                'token': access_token
            }, 200
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError
