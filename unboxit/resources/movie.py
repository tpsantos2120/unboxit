
from flask import Response, request
from flask.json import jsonify
from flask_jwt_extended.view_decorators import verify_jwt_in_request
from requests.sessions import extract_cookies_to_jar
from unboxit.models.models import Movie, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import DoesNotExist, NotUniqueError
from unboxit.resources.errors import InternalServerError, MovieNotExistsError, MovieAlreadyExistsError
import json
class MoviesApi(Resource):
    @jwt_required(locations=['headers', 'cookies'])
    def get(self):
        identity = get_jwt_identity()
        movies = []
        if identity:  
            user = User.objects.get(id=identity['user_id'])
            for movie in user.movies:
                user_movies = Movie.objects.get(id=movie.id).to_json()
                movies.append(user_movies)
            return Response(movies, mimetype="application/json", status=200)

    @jwt_required(locations=['headers', 'cookies'])
    def post(self):
        identity = get_jwt_identity()
        body = request.form.get('data')
        user = User.objects.get(id=identity['user_id'])
        movie = Movie(**json.loads(body), added_by=user)
        movie.save()
        user.update(add_to_set__movies=movie)
        user.save()
        return {'message': "Movie added successfully!"}, 200
 

