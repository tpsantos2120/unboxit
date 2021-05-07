from flask import make_response, url_for, render_template
from flask_jwt_extended import JWTManager
from werkzeug.utils import redirect

jwt = JWTManager()


def initialize_jwt(app):
    """
        Register the JWT instance with the Flask app.
    """
    jwt.init_app(app)


@jwt.unauthorized_loader
def not_authorized(callback):
    """
        Handle 401 errors with redirect
        when token does not exist.
    """
    return make_response(render_template(
        "components/401.html"))


@jwt.expired_token_loader
def expired_token(jwt_header, payload):
    """
        Handle 401 errors with redirect
        when token does not exist.
    """
    return make_response(render_template(
        "components/401.html"))


@jwt.token_verification_failed_loader
def token_verification_failed(jwt_header, payload):
    """
        Handle 401 errors with redirect
        when token does not exist.
    """
    return make_response(render_template(
        "components/401.html"))


@jwt.invalid_token_loader
def invalid_token(callback):
    """
        Handle 401 errors with redirect
        when token does not exist.
    """
    return make_response(render_template(
        "components/401.html"))
