from flask import Response, request, render_template, make_response, url_for, session
from flask_restful import Resource

class Dashboard(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('views/dashboard.html'),200,headers)