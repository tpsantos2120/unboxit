from flask import Response, request, render_template, make_response, url_for, redirect
from flask_restful import Resource
import requests, os

class GetMoviesByTitle(Resource):
    def get(self, title):
        print(title)
        configs = GetIMDBConfigs()
        url = configs.get_url()
        headers = configs.get_headers()
        querystring = {"type": "get-movies-by-title", "title": "matrix"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()

class GetMovieDetails(Resource):
    def get(self, id):
        configs = GetIMDBConfigs()
        url = configs.get_url()
        headers = configs.get_headers()
        querystring = {"type": "get-movie-details", "imdb": "tt2935510"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()

class GetMovieImages(Resource):
    def get(self, id):
        configs = GetIMDBConfigs()
        url = configs.get_url()
        headers = configs.get_headers()
        querystring = {"type": "get-movies-images-by-imdb", "imdb": "tt2935510"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()

class GetSimilarMovies(Resource):
    def get(self, id):
        configs = GetIMDBConfigs()
        url = configs.get_url()
        headers = configs.get_headers()
        querystring = {"type": "get-similar-movies", "imdb": "tt2935510","page":"1"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()

class GetShowsByTitle(Resource):
    def get(self, title):
        configs = GetIMDBConfigs()
        url = configs.get_url()
        headers = configs.get_headers()
        querystring = {"type": "get-shows-by-title", "title": "thrones"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()

class GetShowDetails(Resource):
    def get(self, id):
        configs = GetIMDBConfigs()
        url = configs.get_url()
        headers = configs.get_headers()
        querystring = {"type": "get-show-details", "imdb": "tt2741602"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()

class GetShowImages(Resource):
    def get(self, id):
        configs = GetIMDBConfigs()
        url = configs.get_url()
        headers = configs.get_headers()
        querystring = {"type": "get-show-images-by-imdb", "imdb": "tt2741602"}
        response = requests.request("GET", url, headers=headers, params=querystring)
        return response.json()

class GetSimilarShows(Resource):
    def get(self, id):
        configs = GetIMDBConfigs()
        url = configs.get_url()
        headers = configs.get_headers()
        querystring = {"type": "get-similar-shows", "imdb": "tt2741602","page":"1"}
        response = requests.request("GET", url, headers=headers, params=querystring)
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