
from flask import Response, request
from flask.json import jsonify
from unboxit.models.models import Movie, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import DoesNotExist, NotUniqueError
from unboxit.resources.errors import InternalServerError, MovieNotExistsError, MovieAlreadyExistsError

class MoviesApi(Resource):
    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)

    @jwt_required(locations=['headers', 'cookies'])
    def post(self):
        try:
            user_id = get_jwt_identity(locations=['headers', 'cookies'])
            body = request.get_json()
            print(body)
            user = User.objects.get(id=user_id)
            movie = Movie(**body, added_by=user)
            movie.save()
            user.update(add_to_set__movies=movie)
            user.save()
            id = movie.id
            return {'id': str(id)}, 200
        except DoesNotExist:
            raise MovieNotExistsError
        except NotUniqueError:
            raise MovieAlreadyExistsError
        except Exception as e:
            raise InternalServerError
