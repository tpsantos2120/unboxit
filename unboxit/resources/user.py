import datetime
from unboxit.services.mail_service import send_email
from flask import Response, request, render_template
from flask.helpers import make_response
from flask_jwt_extended import create_access_token
from flask_jwt_extended.utils import get_jwt_identity, set_access_cookies
from flask_jwt_extended.view_decorators import jwt_required
from unboxit.models.models import User
from flask_restful import Resource
from jwt.exceptions import ExpiredSignatureError, DecodeError, InvalidTokenError
from mongoengine.errors import DoesNotExist, FieldDoesNotExist, NotUniqueError
from unboxit.resources.errors import EmailDoesNotExistsError, InternalServerError, \
    UnauthorizedError, SchemaValidationError, EmailAlreadyExistsError, BadTokenError


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
    def post(self):
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
        except ExpiredSignatureError:
            raise ExpiredSignatureError
        except (DecodeError, InvalidTokenError):
            raise BadTokenError
        except Exception as e:
            raise InternalServerError


class ForgotPassword(Resource):
    def post(self):
        try:
            url = request.host_url + 'reset/password/'
            body = request.get_json()
            email = body.get('email')
            if not email:
                raise SchemaValidationError

            user = User.objects.get(email=email)
            if not user:
                raise EmailDoesNotExistsError

            expires = datetime.timedelta(hours=24)
            payload = {"user_id": str(user.id)}
            reset_token = create_access_token(payload, expires_delta=expires)

            return send_email('[Unboxit] Reset Your Password',
                              sender='contact@tsantos.dev',
                              recipients=[user.email],
                              text_body=render_template('components/reset_password.txt',
                                                        url=url + reset_token),
                              html_body=render_template('components/reset_password.html',
                                                        url=url + reset_token, first_name=user.first_name))
        except SchemaValidationError:
            raise SchemaValidationError
        except DoesNotExist:
            raise EmailDoesNotExistsError
        except Exception as e:
            raise InternalServerError
