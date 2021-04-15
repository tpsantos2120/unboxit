from werkzeug.exceptions import HTTPException

class InternalServerError(HTTPException):
    pass
class MovieNotExistsError(HTTPException):
    pass

class MovieAlreadyExistsError(HTTPException):
    pass
class MovieAlreadyExistsError(HTTPException):
    pass
class UnauthorizedError(HTTPException):
    pass

errors = {
    "InternalServerError": {
        "message": "Something went wrong internally",
        "status": 500
    },
     'MovieNotExistsError': {
         'message': "Movie with given id doesn't exist",
         'status': 400
     },
     "MovieAlreadyExistsError": {
         "message": "Movie with given id already exists",
         "status": 400
     },
      "UnauthorizedError": {
         "message": "Invalid username or password",
         "status": 401
     }
}