from flask import Response, request, render_template, make_response, url_for, redirect
from flask_restful import Resource
import requests, os

class GetMoviesByTitle(Resource):
    def get(self):
        configs = GetIMDBConfigs()
        url = configs.get_url()
        print(url)
        headers = configs.get_headers()
        print(headers)
        querystring = {"type": "get-movies-by-title", "title": "matrix"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)
        return response.json()

class GetMovieDetails(Resource):
    def get(self):
        configs = GetIMDBConfigs()
        url = configs.get_url()
        print(url)
        headers = configs.get_headers()
        print(headers)
        querystring = {"type": "get-movie-details", "imdb": "tt2935510"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)
        return response.json()

class GetMovieImages(Resource):
    def get(self):
        configs = GetIMDBConfigs()
        url = configs.get_url()
        print(url)
        headers = configs.get_headers()
        print(headers)
        querystring = {"type": "get-movies-images-by-imdb", "imdb": "tt2935510"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)
        return response.json()

class GetSimilarMovies(Resource):
    def get(self):
        configs = GetIMDBConfigs()
        url = configs.get_url()
        print(url)
        headers = configs.get_headers()
        print(headers)
        querystring = {"type": "get-similar-movies", "imdb": "tt2935510","page":"1"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        print(response.text)
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
        return  self.url 