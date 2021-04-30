from unboxit.models.models import Watchlist
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
            Dashboard.cache_data()
            print("done")
            watchlist_cache, recommendation_cache, trending_movies_cache = cache.get_many(
                "watchlist_cache", "recommendation_cache", "trending_movies_cache")
            return make_response(render_template('views/dashboard.html',
                                                 trending_movies=trending_movies_cache,
                                                 watchlist=watchlist_cache,
                                                 recommendation=recommendation_cache,
                                                 title="Dashboard",
                                                 logged_in=True,
                                                 first_name=identity['first_name'],
                                                 last_name=identity['last_name']))
        else:
            return redirect(url_for('home'))

    def fetch_watchlist():
        recommend = []
        watchlist = []
        token = request.cookies.get('access_token_cookie')
        headers = {"Authorization": "Bearer " + token}
        watchlist_response = requests.get(
            request.url_root + 'api/watchlists', headers=headers).json()
        watchlist_data = watchlist_response
        for data in watchlist_data:
            recommend.append({"id": json.loads(data).get(
                "imdb_id"), "type": json.loads(data).get("media_type")})
            watchlist.append(json.loads(data))
        cache.set("recommend", recommend)
        return watchlist

    def fetch_trending_movies():
        trending_movies_response = requests.get(
            request.url_root + 'search/trending/movies')
        trending_movies = trending_movies_response.json()
        return trending_movies

    def fetch_recommendations():
        recommend = cache.get("recommend")
        if len(recommend) > 0:
            data = random.choice(recommend)
            recommendations_response = requests.post(
                request.url_root + 'recommend', data=data)
            recommendations = recommendations_response.json()
            return recommendations

    def cache_data():
        watchlist_cache, recommendation_cache, trending_movies_cache = cache.get_many(
            "watchlist_cache", "recommendation_cache", "trending_movies_cache")
        if watchlist_cache == None and recommendation_cache == None and trending_movies_cache == None:
            watchlist_cache = Dashboard.fetch_watchlist()
            recommendation_cache = Dashboard.fetch_recommendations()
            trending_movies_cache = Dashboard.fetch_trending_movies()
            cache.set_many({'watchlist_cache': watchlist_cache,
                            'recommendation_cache': recommendation_cache,
                            'trending_movies_cache': trending_movies_cache})
        elif len(watchlist_cache) > 0:
            print(len(watchlist_cache))
            recommendation_cache = Dashboard.fetch_recommendations()
            cache.set("recommendation_cache", recommendation_cache)
        elif len(watchlist_cache) == 0:
            cache.delete("recommendation_cache")
       
     

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
