import os
from unboxit.resources.jwt import initialize_jwt
from flask import Flask
from flask import render_template
from unboxit.models.db import initialize_db
from flask_restful import Api
from flask_bcrypt import Bcrypt
from unboxit.resources.errors import errors
from flask_mail import Mail
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': os.environ.get("MONGO_URI"),
}
app.secret_key = os.environ.get("SECRET_KEY")

def page_not_found(e):
  return render_template('components/error.html'), 404

app.register_error_handler(404, page_not_found)

from unboxit.resources.routes import initialize_routes

mail = Mail(app)
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)


initialize_jwt(app)
initialize_db(app)
initialize_routes(api)

