from flask import request, render_template, make_response
from flask_restful import Resource


class ForgotPasswordReset(Resource):
    def get(self, token):
        print(token)
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('views/forgot_password.html', title="Password Reset"),200,headers)

# class ForgotPasswordReset(Resource):
#     def get(self, token):
#         print(token)
#         headers = {'Content-Type': 'text/html'}
#         return make_response(render_template('views/forgot_password_view.html', title="Password Reset"),200,headers)