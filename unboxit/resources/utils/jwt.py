from flask.helpers import make_response, url_for
from flask_jwt_extended import JWTManager
from werkzeug.utils import redirect

jwt = JWTManager()


def initialize_jwt(app):
    """
        Register the JWT instance with the Flask app.
    """
    jwt.init_app(app)
