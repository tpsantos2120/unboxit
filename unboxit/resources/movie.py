
from flask import Response, request
from unboxit.models.models import Movie
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource


class MoviesApi(Resource):
    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)
    
    def post(self):
        body = request.get_json()
        movie = Movie(**body).save()
        id = movie.id
        return {'id': str(id)}, 200
