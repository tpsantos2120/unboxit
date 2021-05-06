from .jwt import jwt
from flask.helpers import make_response, url_for
from werkzeug.utils import redirect


@jwt.unauthorized_loader
def not_authorized(callback):
    """
        Handle 401 errors with redirect 
        when token does not exist.
    """
    return make_response(redirect(url_for('home')))
