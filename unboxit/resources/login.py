
from flask import Response, request, render_template, make_response, url_for, session, redirect
from flask_jwt_extended.utils import set_access_cookies
from flask_restful import Resource
import requests


class Login(Resource):
    def post(self):
        body = request.form
        url_root = request.url_root
        response = requests.post(url_root + 'api/auth/login',
                                 data={'email': body.get('login-email'),
                                       'password': body.get('login-password')
                                       })
        json_response = response.json()
        if response.status_code == 200:
            res = make_response(redirect(url_for('dashboard')))
            set_access_cookies(res, json_response["token"])
            return res
        else:
            return redirect(url_for('home'))
