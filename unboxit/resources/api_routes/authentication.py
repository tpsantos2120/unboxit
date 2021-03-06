import datetime
from unboxit.services.mail_service import send_email
from flask import request, render_template, make_response
from flask_jwt_extended import create_access_token, decode_token,\
    get_jwt_identity, set_access_cookies, jwt_required
from unboxit.models.models import User
from flask_restful import Resource
from jwt.exceptions import ExpiredSignatureError, DecodeError, \
    InvalidTokenError
from mongoengine.errors import DoesNotExist, FieldDoesNotExist, \
    NotUniqueError
from unboxit.resources.utils.errors import EmailDoesNotExistsError, \
    ExpiredTokenError, InternalServerError, UnauthorizedError, \
    SchemaValidationError, EmailAlreadyExistsError, BadTokenError


class RegisterUserApi(Resource):
    """
        Make this a Resource by extending Flask Restfull Resource class,
        then this resource be executed when the methods it has match
        a HTTP request method.
    """

    def post(self):
        """
            Insert user details to Mongo via POST and handle possible excepts
            that might entail.
        """
        try:
            body = request.get_json()
            user = User(**body)
            user.hash_password()
            user.save()
            expires = datetime.timedelta(days=7)
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
    """
        Make this a Resource by extending Flask Restfull Resource class,
        then this resource be executed when the methods it has match
        a HTTP request method.
    """

    def post(self):
        """
            Make post requests to Mongo to login a user and generate JWT token.
            Handle exceptions Mongo might throw depending on how request is
            sent.
        """
        try:
            body = request.get_json()
            user = User.objects.get(email=body.get('email'))
            authorized = user.check_password(body.get('password'))
            if not authorized:
                raise UnauthorizedError
            expires = datetime.timedelta(days=7)
            user_details = {
                "user_id": str(user.id),
                "first_name": user.first_name,
                "last_name": user.last_name
            }
            access_token = create_access_token(
                identity=user_details, expires_delta=expires)
            res = make_response({
                "response": "You have logged in successfully.",
                'token': access_token,
                'status': 200
            }, 200)
            set_access_cookies(res, access_token)
            return res
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception as e:
            raise InternalServerError


class ResetPassword(Resource):
    """
        Make this a Resource by extending Flask Restfull Resource class,
        then this resource be executed when the methods it has match
        a HTTP request method.
    """
    @jwt_required(locations=['headers', 'cookies'])
    def post(self):
        """
            Reset password request when user is logged in via the
            seetings navbar menu.Handle exceptions if there
            is any and protect route.
        """
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
            raise ExpiredTokenError
        except (DecodeError, InvalidTokenError):
            raise BadTokenError
        except Exception as e:
            raise InternalServerError


class ResetFogottenPassword(Resource):
    """
        Make this a Resource by extending Flask Restfull Resource class,
        then this resource be executed when the methods
        it has match a HTTP request method.
    """
    @jwt_required(locations=['headers'])
    def post(self):
        """
            Handle password change when user not logged in,
            check for token and if all good update.
        """
        try:
            body = request.get_json()
            bearer = request.headers.get('Authorization')
            base_url = request.url_root
            token = bearer.split()[1]
            password = body.get('password')

            if not token or not password:
                raise SchemaValidationError

            user_id = decode_token(token)['sub']['user_id']

            user = User.objects.get(id=user_id)

            user.modify(password=password)
            user.hash_password()
            user.save()

            return send_email('[Unboxit] Password reset successful',
                              sender='contact@tsantos.dev',
                              recipients=[user.email],
                              text_body='Password Reset',
                              html_body=render_template(
                                  'components/reset_password_response.html',
                                  first_name=user.first_name,
                                  base_url=base_url))

        except SchemaValidationError:
            raise SchemaValidationError
        except ExpiredSignatureError:
            raise ExpiredTokenError
        except (DecodeError, InvalidTokenError):
            raise BadTokenError
        except Exception as e:
            raise InternalServerError


class ForgotPassword(Resource):
    """
        Make this a Resource by extending Flask Restfull Resource class,
        then this resource be executed when the methods
        it has match a HTTP request method.
    """

    def post(self):
        """
            Upon user request send user email with password reset link.
        """
        try:
            url = request.host_url + 'reset/password/'
            body = request.get_json()
            base_url = request.url_root
            email = body.get('email')

            if not email:
                raise SchemaValidationError

            user = User.objects.get(email=email)
            if not user:
                raise EmailDoesNotExistsError

            expires = datetime.timedelta(minutes=60)
            payload = {"user_id": str(user.id)}
            reset_token = create_access_token(payload, expires_delta=expires)

            return send_email('[Unboxit] Reset Your Password',
                              sender='contact@tsantos.dev',
                              recipients=[user.email],
                              text_body=render_template(
                                  'components/reset_password.txt',
                                  url=url + reset_token),
                              html_body=render_template(
                                  'components/reset_password.html',
                                  url=url + reset_token,
                                  first_name=user.first_name,
                                  base_url=base_url))
        except SchemaValidationError:
            raise SchemaValidationError
        except DoesNotExist:
            raise EmailDoesNotExistsError
        except Exception as e:
            raise InternalServerError
