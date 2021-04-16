from flask import Response, request, render_template, make_response, url_for, session, redirect
from flask_restful import Resource

class Dashboard(Resource):
    def get(self):
        cookie_exist = request.cookies.get('token')
        if cookie_exist:
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template('views/dashboard.html'),200,headers)
        else:
            return redirect(url_for('home'))