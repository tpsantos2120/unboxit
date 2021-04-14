
from flask import Response, request
from flask.json import jsonify
from unboxit.models.models import Movie, User
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from mongoengine.errors import DoesNotExist
from unboxit.resources.errors import InternalServerError, MovieNotExistsError

class MoviesApi(Resource):
    def get(self):
        movies = Movie.objects().to_json()
        return Response(movies, mimetype="application/json", status=200)

    @jwt_required()
    def post(self):
        try:
            print()
            user_id = get_jwt_identity()
            body = request.get_json()
            user = User.objects.get(id=user_id)
            check_movie = Movie.objects.get(imdb_id=body['imdb_id'])
            # if not check_movie:
            #     print(check_movie)
            #movie =  Movie(**body)
            # movie.save()
            # user.update(push__movies=movie)
            # user.save()
            #id = movie.id
            return {'id': "str(id)"}, 200
        except DoesNotExist:
            raise MovieNotExistsError
        except Exception as e:
            raise InternalServerError
