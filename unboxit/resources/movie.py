
from flask import Response
from unboxit.models.models import Movie
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource


class MoviesApi(Resource):
    def get(self):
        query = Movie.objects()
        movies = Movie.objects().to_json()
        print(movies)
        print(query)
        return Response(movies, mimetype="application/json", status=200)
