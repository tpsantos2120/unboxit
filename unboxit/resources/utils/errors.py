from werkzeug.exceptions import HTTPException


class InternalServerError(HTTPException):
    """
        Customize errors by letting them pass and not throwing
        the default errors.
    """
    pass


class EntryNotExistsError(HTTPException):
    """
        Customize errors by letting them pass and not throwing
        the default errors.
    """
    pass


class EntryAlreadyExistsError(HTTPException):
    """
        Customize errors by letting them pass and not throwing
        the default errors.
    """
    pass


class EntryAlreadyExistsError(HTTPException):
    """
        Customize errors by letting them pass and not throwing
        the default errors.
    """
    pass


class UnauthorizedError(HTTPException):
    """
        Customize errors by letting them pass and not throwing
        the default errors.
    """
    pass


class EmailAlreadyExistsError(HTTPException):
    """
        Customize errors by letting them pass and not throwing
        the default errors.
    """
    pass


class SchemaValidationError(HTTPException):
    """
        Customize errors by letting them pass and not throwing
        the default errors.
    """
    pass


class EmailDoesNotExistsError(HTTPException):
    """
        Customize errors by letting them pass and not throwing
        the default errors.
    """
    pass


class SchemaValidationError(HTTPException):
    """
        Customize errors by letting them pass and not throwing
        the default errors.
    """
    pass


class BadTokenError(HTTPException):
    """
        Customize errors by letting them pass and not throwing
        the default errors.
    """
    pass


class ExpiredTokenError(HTTPException):
    """
        Customize errors by letting them pass and not throwing
        the default errors.
    """
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
