import os
from flask import Flask
from flask import render_template
from unboxit.models.db import initialize_db
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from unboxit.resources.errors import errors

app = Flask(__name__)
app.config.from_pyfile('env.py')
app.config['MONGODB_SETTINGS'] = {
    'host': os.environ.get('MONGO_URI')
}
app.secret_key = os.environ.get("SECRET_KEY")

def page_not_found(e):
  return render_template('views/error.html'), 404

app.register_error_handler(404, page_not_found)

from unboxit.resources.routes import initialize_routes

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

initialize_db(app)
initialize_routes(api)