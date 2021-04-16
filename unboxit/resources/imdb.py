from flask import Response, request, render_template, make_response, url_for, redirect
from flask_restful import Resource
import requests, os


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