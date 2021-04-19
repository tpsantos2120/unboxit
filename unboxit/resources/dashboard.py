from flask import Response, request, render_template, make_response, url_for, session, redirect
from flask_restful import Resource
import requests

class Dashboard(Resource):
    def get(self):
        cookie_exist = request.cookies.get('token')
        if cookie_exist:
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template('views/dashboard.html', title="Dashboard", logged_in=True),200,headers)
        else:
            return redirect(url_for('home'))

class ViewDetails(Resource):
    def get(self):
        id = request.args.get('id')
        query_type = request.args.get('type')
        print(query_type,id)
        if query_type == "Movies":
            response = requests.request(
                    "GET", request.url_root + "/get-movie-details/"+id)
            result_details = response.json()
        elif query_type =="TV Shows":
            response = requests.request(
                    "GET", request.url_root + "/get-show-details/"+id)
            result_details = response.json()
        print(result_details)
        if result_details:
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template('views/view_details.html', result=result_details),200,headers)

class DashboardSearch(Resource):
    def get(self):
        cookie_exist = request.cookies.get('token')
        if cookie_exist:
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template('views/dashboard_search.html', title="Dashboard Search", logged_in=True),200,headers)
        else:
            return redirect(url_for('home'))