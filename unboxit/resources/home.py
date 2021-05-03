
from flask import Response, request, render_template, make_response, url_for, redirect
from flask_jwt_extended.view_decorators import verify_jwt_in_request
from flask_restful import Resource
from .jwt import jwt


class Home(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('views/home.html', title="Homepage"), 200, headers)
