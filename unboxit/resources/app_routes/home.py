
from flask import render_template, make_response
from flask.helpers import url_for
from flask_jwt_extended.utils import get_jwt_identity
from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource
from werkzeug.utils import redirect


class Home(Resource):
    """
        Render home page route.
    """
    @jwt_required(locations=['headers', 'cookies'], optional=True)
    def get(self):
        """
            Render home page if identidy cannot be verified or
            reirect to dashboard.
        """
        identity = get_jwt_identity()
        if not identity:
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template('views/home.html',
                                                 title="Homepage"),
                                 200,
                                 headers)
        else:
            return make_response(redirect(url_for('dashboard')))
