
from flask import Response, request, render_template, make_response
from flask_restful import Resource

class Home(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('views/home.html'),200,headers)
    def post(self):
        body = request.get_json()
        return {"render":body}