from flask import Flask
from unboxit.models.db import initialize_db
from flask_restful import Api


app = Flask(__name__)
app.config.from_pyfile('env.py')


from unboxit.resources.routes import initialize_routes


api = Api(app)


initialize_db(app)
initialize_routes(api)