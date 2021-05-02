from werkzeug.exceptions import HTTPException


class InternalServerError(HTTPException):
    pass


class EntryNotExistsError(HTTPException):
    pass


class EntryAlreadyExistsError(HTTPException):
    pass


class EntryAlreadyExistsError(HTTPException):
    pass


class UnauthorizedError(HTTPException):
    pass


class EmailAlreadyExistsError(HTTPException):
    pass


class SchemaValidationError(HTTPException):
    pass


class EmailDoesNotExistsError(HTTPException):
    pass


class SchemaValidationError(HTTPException):
    pass


class BadTokenError(HTTPException):
    pass


class ExpiredTokenError(HTTPException):
    pass


errors = {
    "InternalServerError": {
        "message": "Something went wrong internally",
        "status": 500
    },
    'EntryNotExistsError': {
        'message': "Entry with given id doesn't exist",
        'status': 400
    },
    "EntryAlreadyExistsError": {
        "message": "Entry has already been added.",
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
    "EmailDoesNotExistsError": {
        "message": "Couldn't find the user with given email address",
        "status": 400
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400
    },
    "BadTokenError": {
        "message": "Invalid token",
        "status": 403
    },
    "ExpiredTokenError": {
        "message": "Expired token",
        "status": 403
    }
}
