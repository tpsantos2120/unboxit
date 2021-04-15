
from flask import Response, request, render_template, make_response, url_for, session, redirect
from flask_restful import Resource
import requests


class Login(Resource):
    def post(self):
        body = request.form
        url_root = request.url_root
        response = requests.post(url_root + 'api/auth/login',
                                 data={'email': body.get('email'),
                                       'password': body.get('password')
                                       })
        json_response = response.json()
        print(json_response["token"])
        if response.status_code == 200:
            res = make_response(redirect(url_for('dashboard')))
            res.set_cookie('token', json_response["token"], httponly=True)
            return res
        else:
            return redirect(url_for('home'))
