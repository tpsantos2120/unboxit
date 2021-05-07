import os
from unboxit.resources.app_routes.error_handler import ErrorHandler
from .config import ProductionConfig, DevelopmentConfig, TestingConfig
from unboxit.resources.utils.cache import initialize_cache
from unboxit.resources.utils.jwt import initialize_jwt
from flask import Flask
from unboxit.models.db import initialize_db
from flask_restful import Api
from flask_bcrypt import Bcrypt
from unboxit.resources.utils.errors import errors
from flask_mail import Mail
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()

"""
    Set configurations based on what the ENV variable holds.
    Production, Testing and Development.
"""
if os.environ.get("ENV") == "production":
    app.config.from_object(ProductionConfig())
elif os.environ.get("ENV") == "development":
    app.config.from_object(DevelopmentConfig())
else:
    app.config.from_object(TestingConfig())

mail = Mail(app)

app.register_error_handler(404, ErrorHandler.page_not_found)
app.register_error_handler(500, ErrorHandler.internal_error)


api = Api(app, errors=errors)
bcrypt = Bcrypt(app)


"""
    This import here is because the routes has to be imported
    after Restful initiallization, otherwise there is circular issues.
"""
with app.app_context():
    from unboxit.resources.routes.routes import initialize_routes

initialize_jwt(app)
initialize_db(app)
initialize_cache(app)
initialize_routes(api)
