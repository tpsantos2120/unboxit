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


class EmailAlreadyExistsError(HTTPException):
    pass


class SchemaValidationError(HTTPException):
    pass


class EmailDoesnotExistsError(Exception):
    pass


class SchemaValidationError(Exception):
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
        "message": "Movie has already been added.",
        "status": 400
    },
    "UnauthorizedError": {
        "message": "Invalid username or password",
        "status": 401
    },
    "EmailAlreadyExistsError": {
        "message": "User with given email address already exists",
        "status": 400
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    },
    "EmailDoesnotExistsError": {
        "message": "Couldn't find the user with given email address",
        "status": 400
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    }
}
