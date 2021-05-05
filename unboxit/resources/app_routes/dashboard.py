from flask import request, render_template, make_response, url_for, redirect
from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from flask_jwt_extended import jwt_required
from unboxit.resources.utils.cache import cache
import requests
import random


class Dashboard(Resource):
    """
        Make this a Resource by extending Flask Restfull Resource class,
        then this resource be executed when the methods it has match a HTTP request method. 
    """
    @jwt_required(locations=['headers', 'cookies'])
    def get(self):
        """
            GET request to load dashboard if token exists and generate view 
            with watchlist, recommendations and trending. Cache results from DB.
        """
        cookie_exist = verify_jwt_in_request(locations=['headers', 'cookies'])
        identity = get_jwt_identity()
        if cookie_exist:
            Dashboard.cache_data()
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

    def fetch_watchlist():
        """
            Get watchlist iterate through IDs cache them
            for the fetch recommendations. Cache whataver the 
            DB gives back.
        """
        recommend = []
        watchlist = []
        token = request.cookies.get('access_token_cookie')
        headers = {"Authorization": "Bearer " + token}
        watchlist_response = requests.get(
            request.url_root + 'api/watchlists', headers=headers).json()
        watchlist_data = watchlist_response
        if watchlist_data:
            for data in watchlist_data:
                recommend.append(
                    {"id": data["imdb_id"], "type": data["media_type"]})
                watchlist.append(data)
            cache.set("recommend", recommend)
            return watchlist
        else:
            cache.set("recommend", recommend)
            return watchlist

    def fetch_trending_movies():
        """
            Query IMDB for trending shows and movies.
        """
        trending_movies_response = requests.get(
            request.url_root + 'search/trending/movies').json()
        trending_movies = trending_movies_response
        return trending_movies

    def fetch_recommendations():
        """
            Recommend as long as there is at least one watchlist document.
        """
        recommend = cache.get("recommend")
        if not recommend == None and len(recommend) > 0:
            data = random.choice(recommend)
            recommendations_response = requests.post(
                request.url_root + 'recommend', data=data)
            if recommendations_response.status_code == 200:
                recommendations = recommendations_response.json()
                return recommendations
            if recommendations_response.status_code == 400:
                recommend.remove(data)
                cache.set("recommend", recommend)
                return Dashboard.fetch_recommendations()
        else:
            recommend = []
            cache.set("recommend", recommend)
            return recommend

    def cache_data():
        """
            Executed when dashboard is loaded, make sure caches exists,
            check also if watchlist has records if yes recommend if not
            do not recommend.
        """
        watchlist_cache, recommendation_cache, trending_movies_cache = cache.get_many(
            "watchlist_cache", "recommendation_cache", "trending_movies_cache")

        if watchlist_cache == None:
            watchlist_cache = Dashboard.fetch_watchlist()
            cache.set('watchlist_cache', watchlist_cache)

        if recommendation_cache == None:
            recommendation_cache = Dashboard.fetch_recommendations()
            cache.set('recommendation_cache', recommendation_cache)

        if trending_movies_cache == None:
            trending_movies_cache = Dashboard.fetch_trending_movies()
            cache.set('trending_movies_cache', trending_movies_cache)

        if len(watchlist_cache) > 0:
            if not len(recommendation_cache) > 0:
                recommendation_cache = Dashboard.fetch_recommendations()
            cache.set("recommendation_cache", recommendation_cache)
        elif len(watchlist_cache) == 0:
            cache.delete("recommendation_cache")


class DashboardSearch(Resource):
    """
        Make this a Resource by extending Flask Restfull Resource class,
        then this resource be executed when the methods it has match a HTTP request method. 
    """
    @jwt_required(locations=['headers', 'cookies'])
    def get(self):
        """
            Load dashboard search, ensure cache exists for 
            watchlist, recommend and trending.
        """
        cookie_exist = verify_jwt_in_request(locations=['headers', 'cookies'])
        if cookie_exist:
            watchlist_cache, recommendation_cache, trending_movies_cache = cache.get_many(
                "watchlist_cache", "recommendation_cache", "trending_movies_cache")
            if watchlist_cache == None:
                watchlist_cache = Dashboard.fetch_watchlist()
                cache.set('watchlist_cache', watchlist_cache)
            if recommendation_cache == None:
                recommendation_cache = Dashboard.fetch_recommendations()
                cache.set('recommendation_cache', recommendation_cache)
            if trending_movies_cache == None:
                trending_movies_cache = Dashboard.fetch_trending_movies()
                cache.set('trending_movies_cache', trending_movies_cache)
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template('views/dashboard_search.html', title="Dashboard Search", logged_in=True), 200, headers)
        else:
            return redirect(url_for('home'))
