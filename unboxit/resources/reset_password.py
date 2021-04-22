from flask.helpers import make_response
from unboxit.resources.errors import EmailDoesnotExistsError, SchemaValidationError
from flask_restful import Resource
from flask import request, render_template
from unboxit.models.models import User
from unboxit.services.mail_service import send_email
from flask_jwt_extended import create_access_token, decode_token

import datetime


class ForgotPassword(Resource):
    def post(self):
        url = request.host_url + 'reset/'

        body = request.get_json()
        email = body.get('email')
        if not email:
            raise {"email": "not exist"}

        user = User.objects.get(email=email)
        if not user:
            raise EmailDoesnotExistsError
        expires = datetime.timedelta(hours=24)
        reset_token = create_access_token(str(user.id), expires_delta=expires)

        return send_email('[Unboxit] Reset Your Password',
                          sender='support@unboxit.com',
                          recipients=[user.email],
                          text_body=render_template('components/reset_password.txt',
                                                    url=url + reset_token),
                          html_body=render_template('components/reset_password.html',
                                                    url=url + reset_token))


class ResetPassword(Resource):
    def post(self):
        url = request.host_url + 'reset/'
        body = request.get_json()
        reset_token = body.get('reset_token')
        password = body.get('password')

        if not reset_token or not password:
            raise SchemaValidationError

        user_id = decode_token(reset_token)['identity']
        user = User.objects.get(id=user_id)
        user.modify(password=password)
        user.hash_password()
        user.save()

        return send_email('[Movie-bag] Password reset successful',
                          sender='support@movie-bag.com',
                          recipients=[user.email],
                          text_body='Password reset was successful',
                          html_body='<p>Password reset was successful</p>')


class ResetForm(Resource):
    def post(self, token):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('views/home.html', title="Homapage"), 200, headers)
