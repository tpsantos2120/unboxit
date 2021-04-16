from flask import Response, request, render_template, make_response, url_for, session, redirect
from flask_restful import Resource
import requests


class Register(Resource):
    def post(self):
        body = request.form
        print(body)
        url_root = request.url_root
        response = requests.post(url_root + 'api/auth/register',
                                 data={'first_name': body.get('firstname'),
                                       'last_name': body.get('lastname'),
                                       'username': body.get('username'),
                                       'email': body.get('email'),
                                       'password': body.get('password')
                                       })
        if response:
            print(response.json())
        return {"asd":"redirect(url_for('home'))"}
