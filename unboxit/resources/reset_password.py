from unboxit.resources.errors import EmailDoesnotExistsError
from flask_restful import Resource
from flask import request, render_template
from unboxit.models import User


class ForgotPassword(Resource):
    def post(self):
        url = request.host_url + 'reset/'

        body = request.get_json()
        email = body.get('email')
        if not email:
            return {"email":"not exist"}

        user = User.objects.get(email=email)
        if not user:
            raise EmailDoesnotExistsError
