from werkzeug.exceptions import HTTPException


class InternalServerError(HTTPException):
    pass

class MovieNotExistsError(HTTPException):
    pass

errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
     'MovieNotExistsError': {
         'message': "Movie with given id doesn't exists",
         'status': 400
     }
}