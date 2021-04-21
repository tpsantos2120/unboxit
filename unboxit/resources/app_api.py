from flask import request, render_template, make_response, url_for, redirect
from flask_jwt_extended.view_decorators import jwt_required
from flask_restful import Resource
from flask_jwt_extended import verify_jwt_in_request
from .jwt import jwt
import requests


class Dashboard(Resource):
    def get(self):
        cookie_exist = verify_jwt_in_request(locations=['headers', 'cookies'])
        if cookie_exist:
            first_name = cookie_exist[1]['sub']['first_name']
            last_name = cookie_exist[1]['sub']['last_name']
            headers = {
                'Content-Type': 'text/html'
            }
            return make_response(render_template('views/dashboard.html', title="Dashboard",
                                                 logged_in=True, first_name=first_name, last_name=last_name), 200, headers)
        else:
            return redirect(url_for('home'))

    @jwt.expired_token_loader
    def my_expired_token_callback(jwt_header, jwt_payload):
        return redirect(url_for('home'))
    @jwt.unauthorized_loader
    def invalid_token_callback(callback): 
        return redirect(url_for('home'))


class ViewDetails(Resource):
    def get(self):
        id = request.args.get('id')
        query_type = request.args.get('type')
        cookie_exist = request.cookies.get("access_token_cookie")
        logged_in = False
        if cookie_exist:
            logged_in = True
        if query_type and id:
            print(query_type, id)
            if query_type == "Movies":
                response = requests.request(
                    "GET", request.url_root + "/get-movie-details/"+id)
                result_details = response.json()
            elif query_type == "TV Shows":
                response = requests.request(
                    "GET", request.url_root + "/get-show-details/"+id)
                result_details = response.json()
            result_details.pop('status')
            result_details.pop('status_message')
            if result_details:
                headers = {'Content-Type': 'text/html'}
                return make_response(render_template('views/view_details.html', logged_in=logged_in, result=result_details), 200, headers)
        else:
            return redirect(url_for('home'))


class DashboardSearch(Resource):
    def get(self):
        cookie_exist = verify_jwt_in_request(locations=['headers', 'cookies'])
        if cookie_exist:
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template('views/dashboard_search.html', title="Dashboard Search", logged_in=True), 200, headers)
        else:
           
            return redirect(url_for('home'))

    @jwt.expired_token_loader
    def my_expired_token_callback(jwt_header, jwt_payload):
        return redirect(url_for('home'))
