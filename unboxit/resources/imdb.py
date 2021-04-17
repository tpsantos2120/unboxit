from flask import Response, request, render_template, make_response, url_for, redirect
from flask_restful import Resource
from ratelimit import limits, sleep_and_retry
from flask_paginate import Pagination, get_page_parameter
import requests
import os


class GetMoviesByTitle(Resource):
    @sleep_and_retry
    @limits(calls=5, period=1)
    def get(self, title):
        print(title)
        response_result = []
        configs = GetIMDBConfigs()
        url = configs.get_url()
        headers = configs.get_headers()
        query_string = configs.get_query_string(
            request.endpoint, None, title, None)
        query_by_title_response = requests.request(
            "GET", url, headers=headers, params=query_string)
        movies = query_by_title_response.json()
        for movie in movies['movie_results']:
            response = requests.request(
                "GET", request.url_root + "/get-movies-images-by-imdb/"+movie['imdb_id'])
            movies_details = response.json()
            response_result.append(movies_details)
        # page = request.args.get(get_page_parameter(), type=int, default=1)
        # pagination = Pagination(
        #     page=page, total=len(response_result), search=False, record_name='movies')
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('views/movies.html', movies=response_result, view=True))


class GetMovieDetails(Resource):
    @sleep_and_retry
    @limits(calls=5, period=1)
    def get(self, id):
        print(id)
        configs = GetIMDBConfigs()
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
        print(id)
        configs = GetIMDBConfigs()
        url = configs.get_url()
        headers = configs.get_headers()
        query_string = configs.get_query_string(
            request.endpoint, id, None, None)
        print(query_string)
        response = requests.request(
            "GET", url, headers=headers, params=query_string)
        return response.json()


class GetSimilarMovies(Resource):
    def get(self, id):
        print(id)
        configs = GetIMDBConfigs()
        url = configs.get_url()
        headers = configs.get_headers()
        query_string = configs.get_query_string(
            request.endpoint, id, None, "1")
        response = requests.request(
            "GET", url, headers=headers, params=query_string)
        return response.json()


class GetShowsByTitle(Resource):
    def get(self, title):
        print(title)
        response_result = []
        configs = GetIMDBConfigs()
        url = configs.get_url()
        headers = configs.get_headers()
        query_string = configs.get_query_string(
            request.endpoint, None, title, None)
        query_by_title_response = requests.request(
            "GET", url, headers=headers, params=query_string)
        shows = query_by_title_response.json()
        print(shows)
        for show in shows['tv_results']:
            response = requests.request(
                "GET", request.url_root + "/get-show-images-by-imdb/"+show['imdb_id'])
            shows_details = response.json()
            response_result.append(shows_details)
        return response_result


class GetShowDetails(Resource):
    def get(self, id):
        print(id)
        configs = GetIMDBConfigs()
        url = configs.get_url()
        headers = configs.get_headers()
        query_string = configs.get_query_string(
            request.endpoint, id, None, None)
        response = requests.request(
            "GET", url, headers=headers, params=query_string)
        return response.json()


class GetShowImagesByImdb(Resource):
    def get(self, id):
        print(id)
        configs = GetIMDBConfigs()
        url = configs.get_url()
        headers = configs.get_headers()
        query_string = configs.get_query_string(
            request.endpoint, id, None, None)
        print(query_string)
        response = requests.request(
            "GET", url, headers=headers, params=query_string)
        return response.json()


class GetSimilarShows(Resource):
    def get(self, id):
        print(id)
        configs = GetIMDBConfigs()
        url = configs.get_url()
        headers = configs.get_headers()
        query_string = configs.get_query_string(
            request.endpoint, id, None, "1")
        response = requests.request(
            "GET", url, headers=headers, params=query_string)
        return response.json()


class GetIMDBConfigs():
    def get_headers(self):
        self.headers = {
            'x-rapidapi-key': os.environ.get('IMDB_SECRET_KEY'),
            'x-rapidapi-host': os.environ.get('IMDB_API_HOST')
        }
        return self.headers

    def get_url(self):
        self.url = os.environ.get('IMDB_BASE_URL')
        return self.url

    def get_query_string(self, endpoint_type, id, title, page_number):

        if endpoint_type and id and page_number:
            self.query_string = {"type": endpoint_type,
                                 "imdb": id, "page": page_number}
            return self.query_string
        elif endpoint_type and id:
            self.query_string = {"type": endpoint_type, "imdb": id}
            return self.query_string
        elif endpoint_type and title:
            self.query_string = {"type": endpoint_type, "title": title}
            return self.query_string
