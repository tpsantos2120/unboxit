from bson import ObjectId
from flask import request, render_template, make_response, url_for, redirect
from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from flask_jwt_extended import jwt_required
from .jwt import jwt
from .cache import cache
import requests
import json
import random


class Dashboard(Resource):
    @jwt_required(locations=['headers', 'cookies'])
    def get(self):
        cookie_exist = verify_jwt_in_request(locations=['headers', 'cookies'])
        identity = get_jwt_identity()
        if cookie_exist:
            cached_data = Dashboard.cache_data(self)
            return make_response(render_template('views/dashboard.html',
                                                 trending_movies=cached_data['trending_movies'],
                                                 watchlist=cached_data['watchlist'],
                                                 recommendation=cached_data['recommendations'],
                                                 title="Dashboard",
                                                 logged_in=True,
                                                 first_name=identity['first_name'],
                                                 last_name=identity['last_name']))
        else:
            return redirect(url_for('home'))

    def fetch_watchlist(self):
        self.recommend = []
        watchlist = []
        token = request.cookies.get('access_token_cookie')
        headers = {"Authorization": "Bearer " + token}
        watchlist_response = requests.get(
            request.url_root + 'api/movies', headers=headers)
        watchlist_data = watchlist_response.json()
        for data in watchlist_data:
            self.recommend.append({"id": json.loads(data).get(
                'imdb_id'), "type": json.loads(data).get('media_type')})
            watchlist.append(json.loads(data))
        return watchlist

    def fetch_trending_movies():
        trending_movies_response = requests.get(
            request.url_root + 'search/trending/movies')
        trending_movies = trending_movies_response.json()
        return trending_movies

    def fetch_recommendations(self):
        if self.recommend:
            data = random.choice(self.recommend)
        recommendations_response = requests.post(
            request.url_root + 'recommend', data=data)
        recommendations = recommendations_response.json()
        return recommendations

    def cache_data(self):
        if cache.get('data') == None:
            print("does not exist")
            watchlist_cache = Dashboard.fetch_watchlist(self)
            recommendations_cache = Dashboard.fetch_recommendations(self)
            trending_movies_cache = Dashboard.fetch_trending_movies()
            data = {
                "watchlist": watchlist_cache,
                "recommendations": recommendations_cache,
                "trending_movies": trending_movies_cache
            }
            cache.set("data", data)
            return cache.get("data")
        else:
            print("exists")
            return cache.get("data")


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
