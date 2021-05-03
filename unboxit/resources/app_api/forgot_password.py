from flask import render_template, make_response
from flask_restful import Resource


class ForgotPasswordReset(Resource):
    def get(self, token):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('views/forgot_password.html', title="Password Reset"), 200, headers)
