from unboxit.resources.errors import EmailDoesnotExistsError
from flask_restful import Resource
from flask import request, render_template
from unboxit.models import User
from unboxit.services.mail_service import send_email
from flask_jwt_extended import create_access_token

import datetime

class ForgotPassword(Resource):
    def post(self):
        url = request.host_url + 'reset/'

        body = request.get_json()
        email = body.get('email')
        if not email:
            raise {"email":"not exist"}

        user = User.objects.get(email=email)
        if not user:
            raise EmailDoesnotExistsError
        expires = datetime.timedelta(hours=24)
        reset_token = create_access_token(str(user.id), expires_delta=expires)

        return send_email('[Movie-bag] Reset Your Password',
                              sender='support@movie-bag.com',
                              recipients=[user.email],
                              text_body=render_template('email/reset_password.txt',
                                                        url=url + reset_token),
                              html_body=render_template('email/reset_password.html',
                                                        url=url + reset_token))
