
from flask import Response, request, render_template, make_response, url_for, redirect
from flask_restful import Resource

class Home(Resource):
    def get(self):
        cookie_exist = request.cookies.get('token')
        if cookie_exist:
            return redirect(url_for('dashboard'))
        else:    
            headers = {'Content-Type': 'text/html'}
            return make_response(render_template('views/home.html', title="Homapage"),200,headers)
  