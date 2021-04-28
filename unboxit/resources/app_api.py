from bson import ObjectId
from flask import request, render_template, make_response, url_for, redirect
from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource
from flask_jwt_extended import verify_jwt_in_request
from flask_jwt_extended import jwt_required
from .jwt import jwt
import requests
import json, random


class Dashboard(Resource):
    @jwt_required(locations=['headers', 'cookies'])
    def get(self):
        cookie_exist = verify_jwt_in_request(locations=['headers', 'cookies'])
        if cookie_exist:
            watchlist = []
            selected_ids = []
            first_name = cookie_exist[1]['sub']['first_name']
            last_name = cookie_exist[1]['sub']['last_name']
            treding_movies = Dashboard.fetch_treding_movies().json()
            json_data = Dashboard.fetch_watchlist().json()
            for data in json_data:
                selected_ids.append(json.loads(data).get('imdb_id'))
                watchlist.append(json.loads(data))
            if selected_ids:
                print(random.choice(selected_ids))
            return make_response(render_template('views/dashboard.html', trending_movies=treding_movies, watchlist=watchlist, title="Dashboard",
                                                 logged_in=True, first_name=first_name, last_name=last_name))
        else:
            return redirect(url_for('home'))

    def fetch_watchlist():
        token = request.cookies.get('access_token_cookie')
        headers = {"Authorization": "Bearer " + token}
        watchlist_response = requests.get(
            request.url_root + 'api/movies', headers=headers)
        return watchlist_response

    def fetch_treding_movies():
        trending_movies_response = requests.get(
            request.url_root + '/search/trending/movies')
        return trending_movies_response

    def fetch_recommendations(id):
        trending_movies_response = requests.get(
            request.url_root + '/search/trending/movies')
        return trending_movies_response


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
