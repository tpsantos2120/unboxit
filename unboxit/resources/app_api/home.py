
from flask import render_template, make_response
from flask_restful import Resource


class Home(Resource):
    def get(self):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('views/home.html', title="Homepage"), 200, headers)