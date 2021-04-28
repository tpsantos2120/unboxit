from flask import Response, request, render_template, make_response, url_for, redirect, jsonify
from flask_restful import Resource
from ratelimit import limits, sleep_and_retry
import requests
import os


class SearchMovies(Resource):
    """
    Query movies from IMBD API
    """
    @sleep_and_retry
    @limits(calls=5, period=1)
    def get(self, title):
        response_result = []
        imdb = IMDBConfigs()
        url = imdb.get_url()
        headers = imdb.get_headers()
        querystring = {"type": "get-movies-by-title", "title": title}
        response = imdb.request_query(url, headers, querystring)
        movies = response.json()
        if movies['search_results'] > 0:
            for movie in movies['movie_results']:
                querystring = {
                    "type": "get-movies-images-by-imdb", "imdb": movie['imdb_id']}
                response = imdb.request_query(url, headers, querystring)
                movies_images = response.json()
                response_result.append(movies_images)
            headers = {'Content-Type': 'text/html'}
            return make_response(jsonify(render_template('views/view_results.html', type="movies", results=response_result, view=True)), 200, headers)
        else:
            return{"response": "Movie Not Found", "status": 400}


class SearchMovieDetails(Resource):
    @sleep_and_retry
    @limits(calls=5, period=1)
    def get(self, id):
        cookie_exist = request.cookies.get("access_token_cookie")
        logged_in = False
        if cookie_exist:
            logged_in = True
        imdb = IMDBConfigs()
        url = imdb.get_url()
        headers = imdb.get_headers()
        querystring = {
            "type": "get-movie-details", "imdb": id}
        response = imdb.request_query(url, headers, querystring)
        movie_details = response.json()
        movie_details.pop('status')
        movie_details.pop('status_message')
        headers = {'Content-Type': 'text/html'}
        return make_response(jsonify(render_template('components/view_result_details.html', logged_in=logged_in, result=movie_details)), 200, headers)


class SearchTvShows(Resource):
    @sleep_and_retry
    @limits(calls=5, period=1)
    def get(self, title):
        response_result = []
        imdb = IMDBConfigs()
        url = imdb.get_url()
        headers = imdb.get_headers()
        querystring = {"type": "get-shows-by-title", "title": title}
        response = imdb.request_query(url, headers, querystring)
        tv_shows = response.json()
        if tv_shows['search_results'] > 0:
            for show in tv_shows['tv_results']:
                querystring = {
                    "type": "get-show-images-by-imdb", "imdb": show['imdb_id']}
                response = imdb.request_query(url, headers, querystring)
                tv_shows_images = response.json()
                response_result.append(tv_shows_images)
                print(response_result)
            headers = {'Content-Type': 'text/html'}
            return make_response(jsonify(render_template('views/view_results.html', type="shows", results=response_result, view=True)), 200, headers)
        else:
            return{"response": "Movie Not Found", "status": 400}


class SearchShowDetails(Resource):
    @sleep_and_retry
    @limits(calls=5, period=1)
    def get(self, id):
        cookie_exist = request.cookies.get("access_token_cookie")
        logged_in = False
        if cookie_exist:
            logged_in = True
        imdb = IMDBConfigs()
        url = imdb.get_url()
        headers = imdb.get_headers()
        querystring = {
            "type": "get-show-details", "imdb": id}
        response = imdb.request_query(url, headers, querystring)
        tv_show_details = response.json()
        tv_show_details.pop('status')
        tv_show_details.pop('status_message')
        headers = {'Content-Type': 'text/html'}
        return make_response(jsonify(render_template('components/view_result_details.html', logged_in=logged_in, result=tv_show_details)), 200, headers)


class SearchTrendingMovies(Resource):
    @sleep_and_retry
    @limits(calls=5, period=1)
    def get(self):
        response = SearchTrendingMovies.trending_movies()
        movies = response.json()
        trending_movies = []
        for movie in movies['movie_results'][0:10]:
            details = SearchTrendingMovies.trending_movies_details(
                movie['imdb_id'])
            images = SearchTrendingMovies.trending_movies_images(
                movie['imdb_id'])
            trending_details = details.json()
            trending_details['poster'] = images.json()
            trending_movies.append(images.json())
        return trending_movies

    def trending_movies_images(id):
        imdb = IMDBConfigs()
        url = imdb.get_url()
        headers = imdb.get_headers()
        querystring = {
            "type": "get-movies-images-by-imdb", "imdb": id}
        response = imdb.request_query(url, headers, querystring)
        return response

    def trending_movies():
        imdb = IMDBConfigs()
        url = imdb.get_url()
        headers = imdb.get_headers()
        querystring = {
            "type": "get-trending-movies", "page": 1}
        response = imdb.request_query(url, headers, querystring)
        return response

    def trending_movies_details(id):
        imdb = IMDBConfigs()
        url = imdb.get_url()
        headers = imdb.get_headers()
        querystring = {
            "type": "get-movie-details", "imdb": id}
        response = imdb.request_query(url, headers, querystring)
        return response


class SearchTrendingShows(Resource):
    @sleep_and_retry
    @limits(calls=5, period=1)
    def get(self):
        response = SearchTrendingShows.trending_shows()
        shows = response.json()
        trending_shows = []
        for show in shows['tv_results']:
            details = SearchTrendingShows.trending_shows_details(
                show['imdb_id'])
            images = SearchTrendingShows.trending_shows_images(show['imdb_id'])
            trending_details = details.json()
            trending_details['poster'] = images.json().get('poster')
            trending_shows.append(trending_details)
        return trending_shows

    def trending_shows_images(id):
        imdb = IMDBConfigs()
        url = imdb.get_url()
        headers = imdb.get_headers()
        querystring = {
            "type": "get-show-images-by-imdb", "imdb": id}
        response = imdb.request_query(url, headers, querystring)
        return response

    def trending_shows():
        imdb = IMDBConfigs()
        url = imdb.get_url()
        headers = imdb.get_headers()
        querystring = {
            "type": "get-trending-shows", "page": 1}
        response = imdb.request_query(url, headers, querystring)
        return response

    def trending_shows_details(id):
        imdb = IMDBConfigs()
        url = imdb.get_url()
        headers = imdb.get_headers()
        querystring = {
            "type": "get-show-details", "imdb": id}
        response = imdb.request_query(url, headers, querystring)
        return response


class Recommend(Resource):
    @sleep_and_retry
    @limits(calls=5, period=1)
    def get(self):
        body = request.get_json()
        
        return body

    def recommend_shows_images(id):
        imdb = IMDBConfigs()
        url = imdb.get_url()
        headers = imdb.get_headers()
        querystring = {
            "type": "get-show-images-by-imdb", "imdb": id}
        response = imdb.request_query(url, headers, querystring)
        return response

    def recommend_shows_details(id):
        imdb = IMDBConfigs()
        url = imdb.get_url()
        headers = imdb.get_headers()
        querystring = {
            "type": "get-show-details", "imdb": id}
        response = imdb.request_query(url, headers, querystring)
        return response

    def recommend_movies_images(id):
        imdb = IMDBConfigs()
        url = imdb.get_url()
        headers = imdb.get_headers()
        querystring = {
            "type": "get-show-images-by-imdb", "imdb": id}
        response = imdb.request_query(url, headers, querystring)
        return response

    def recommend_movies_details(id):
        imdb = IMDBConfigs()
        url = imdb.get_url()
        headers = imdb.get_headers()
        querystring = {
            "type": "get-show-details", "imdb": id}
        response = imdb.request_query(url, headers, querystring)
        return response


class IMDBConfigs():
    def get_headers(self):
        self.headers = {
            'x-rapidapi-key': os.environ.get('IMDB_SECRET_KEY'),
            'x-rapidapi-host': os.environ.get('IMDB_API_HOST')
        }
        return self.headers

    def get_url(self):
        self.url = os.environ.get('IMDB_BASE_URL')
        return self.url

    def request_query(self, url, headers, query_string):
        if url and headers and query_string:
            response = requests.request(
                "GET", url, headers=headers, params=query_string)
            return response
