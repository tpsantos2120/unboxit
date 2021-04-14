from flask import Response, request
from unboxit.models.models import User
from flask_restful import Resource

class RegisterUserApi(Resource):
    def post(self):
        body = request.get_json()
        user =  User(**body)
        user.save()
        id = user.id
        return {'id': str(id)}, 200