
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
    def get(self):
        cookie_exist = verify_jwt_in_request(locations=['headers', 'cookies'], optional=True)
        if cookie_exist:  
            extract_id = cookie_exist  
            print(cookie_exist[0:3])
            #user = User.objects.get(id=identity['user_id'])
            #print(user.id)
            #movies = Movie.objects(user.movies).to_json()
            #print(movies)
            return Response(cookie_exist, mimetype="application/json", status=200)

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
 

