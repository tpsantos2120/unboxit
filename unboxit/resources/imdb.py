from flask import Response, request, render_template, make_response, url_for, redirect
from flask_restful import Resource
from ratelimit import limits, sleep_and_retry
import requests
import os


class SearchMovies(Resource):
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
            print(headers)
            return make_response(render_template('views/view_search.html', results=response_result, view=True), 200, headers)
        else:
            return{"response": "Movie Not Found", "status_code": 400}


class GetMovieDetails(Resource):
    @sleep_and_retry
    @limits(calls=5, period=1)
    def get(self, id):
        configs = IMDBConfigs()
        url = configs.get_url()
        headers = configs.get_headers()
        query_string = configs.get_query_string(
            request.endpoint, id, None, None)
        response = requests.request(
            "GET", url, headers=headers, params=query_string)
        return response.json()


class GetMoviesImagesByImdb(Resource):
    @sleep_and_retry
    @limits(calls=5, period=1)
    def get(self, id):
        configs = IMDBConfigs()
        url = configs.get_url()
        headers = configs.get_headers()
        query_string = configs.get_query_string(
            request.endpoint, id, None, None)
        response = requests.request(
            "GET", url, headers=headers, params=query_string)
        return response.json()


class GetSimilarMovies(Resource):
    def get(self, id):
        configs = IMDBConfigs()
        url = configs.get_url()
        headers = configs.get_headers()
        query_string = configs.get_query_string(
            request.endpoint, id, None, "1")
        response = requests.request(
            "GET", url, headers=headers, params=query_string)
        return response.json()


class SearchTvShows(Resource):
    def get(self, title):
        response_result = []
        configs = IMDBConfigs()
        url = configs.get_url()
        headers = configs.get_headers()
        query_string = configs.get_query_string(
            request.endpoint, None, title, None)
        query_by_title_response = requests.request(
            "GET", url, headers=headers, params=query_string)
        shows = query_by_title_response.json()
        if not shows['search_results'] == 0:
            for show in shows['tv_results']:
                response = requests.request(
                    "GET", request.url_root + "/get-show-images-by-imdb/"+show['imdb_id'])
                shows_details = response.json()
                response_result.append(shows_details)
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template('views/view_result.html', results=response_result, view=True), 200, headers)
        else:
            return {"response": "Show Not Found", "status_code": 400}


class GetShowDetails(Resource):
    def get(self, id):
        configs = IMDBConfigs()
        url = configs.get_url()
        headers = configs.get_headers()
        query_string = configs.get_query_string(
            request.endpoint, id, None, None)
        response = requests.request(
            "GET", url, headers=headers, params=query_string)
        return response.json()


class GetShowImagesByImdb(Resource):
    def get(self, id):
        configs = IMDBConfigs()
        url = configs.get_url()
        headers = configs.get_headers()
        query_string = configs.get_query_string(
            request.endpoint, id, None, None)
        response = requests.request(
            "GET", url, headers=headers, params=query_string)
        return response.json()


class GetSimilarShows(Resource):
    def get(self, id):
        configs = IMDBConfigs()
        url = configs.get_url()
        headers = configs.get_headers()
        query_string = configs.get_query_string(
            request.endpoint, id, None, "1")
        response = requests.request(
            "GET", url, headers=headers, params=query_string)
        return response.json()


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
