import os
from flask import Flask
from unboxit.models.db import initialize_db
from flask_restful import Api


app = Flask(__name__)
app.config.from_pyfile('env.py')
app.config['MONGODB_SETTINGS'] = {
    'host': os.environ.get('MONGO_URI')
}

from unboxit.resources.routes import initialize_routes


api = Api(app)


initialize_db(app)
initialize_routes(api)