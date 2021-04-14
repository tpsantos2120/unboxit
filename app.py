import os
from flask import Flask
from unboxit.models.db import initialize_db
from flask_restful import Api
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt




app = Flask(__name__)
app.config.from_pyfile('env.py')
app.config['MONGODB_SETTINGS'] = {
    'host': os.environ.get('MONGO_URI')
}
app.secret_key = os.environ.get("SECRET_KEY")

from unboxit.resources.routes import initialize_routes


api = Api(app)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)


initialize_db(app)
initialize_routes(api)