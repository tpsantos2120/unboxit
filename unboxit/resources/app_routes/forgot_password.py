from flask import render_template, make_response
from flask_restful import Resource


class ForgotPasswordReset(Resource):
    """
        Generate view when user clicks on the email reset link.
    """

    def get(self, token):
        """
            Render template for reset password.
        """
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('views/forgot_password.html',
                                             title="Password Reset"),
                             200, headers)
