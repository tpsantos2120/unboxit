
from flask import Response, request
from flask.json import jsonify
from unboxit.models.models import Movie, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import DoesNotExist, NotUniqueError
from unboxit.resources.errors import InternalServerError, MovieNotExistsError, MovieAlreadyExistsError
import json
class MoviesApi(Resource):
    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)

    @jwt_required(locations=['headers', 'cookies'])
    def post(self):
        try:   
            identity = get_jwt_identity()
            body = request.form.get('data')            
            user = User.objects.get(id=identity['user_id'])
            movie = Movie(**json.loads(body), added_by=user)
            movie.save()
            user.update(add_to_set__movies=movie)
            user.save()
            return {'message': "Movie added successfully!"}, 200
        except DoesNotExist:
            raise MovieNotExistsError
        except NotUniqueError:
            print("fuck you")
            raise MovieAlreadyExistsError
        except Exception as e:
            raise InternalServerError
