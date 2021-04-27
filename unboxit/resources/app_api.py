from flask import request, render_template, make_response, url_for, redirect
from flask.json import jsonify
from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended import jwt_required, get_jwt_identity, get_current_user
from .jwt import jwt
import requests, json


class Dashboard(Resource):
    @jwt_required(locations=['headers', 'cookies'])
    def get(self):
        cookie_exist = verify_jwt_in_request(locations=['headers', 'cookies'])
        if cookie_exist:
            first_name = cookie_exist[1]['sub']['first_name']
            last_name = cookie_exist[1]['sub']['last_name']
            token = request.cookies.get('access_token_cookie')
            headers = {"Authorization": "Bearer " + token}
            data_response = requests.get(request.url_root + 'api/movies', headers=headers)
            json_data = data_response.json()
            watchlist = []
            for data in json_data: 
                watchlist.append(json.loads(data))
            return make_response(render_template('views/dashboard.html', watchlist=watchlist, title="Dashboard",
                                                 logged_in=True, first_name=first_name, last_name=last_name), 200, headers)
        else:
            return redirect(url_for('home'))


class DashboardSearch(Resource):
    def get(self):
        cookie_exist = verify_jwt_in_request(locations=['headers', 'cookies'])
        if cookie_exist:
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template('views/dashboard_search.html', title="Dashboard Search", logged_in=True), 200, headers)
        else:
            return redirect(url_for('home'))

    @jwt.expired_token_loader
    def my_expired_token_callback(jwt_header, jwt_payload):
        return redirect(url_for('home'))
