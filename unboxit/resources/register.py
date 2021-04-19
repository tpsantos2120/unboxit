from flask import Response, request, render_template, make_response, url_for, session, redirect
from flask_jwt_extended.utils import set_access_cookies
from flask_restful import Resource
import requests
class Register(Resource):
    def post(self):
        body = request.form
        url_root = request.url_root
        response = requests.post(url_root + 'api/auth/register',
                                 data={'first_name': body.get('firstname'),
                                       'last_name': body.get('lastname'),
                                       'username': body.get('username'),
                                       'email': body.get('email'),
                                       'password': body.get('password')
                                       })
        json_response = response.json()                          
        print(response.status_code)
        if response.status_code == 200:    
            res = make_response(redirect(url_for('dashboard')))
            set_access_cookies(res, json_response["token"])
            return res
        elif response.status_code == 400:
            return {"Error":"Email is not unique" }
        else:
            return redirect(url_for('home'))
