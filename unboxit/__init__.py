import os
from unboxit.resources.cache import initialize_cache
from unboxit.resources.jwt import initialize_jwt
from flask import Flask
from flask import render_template
from unboxit.models.db import initialize_db
from flask_restful import Api
from flask_bcrypt import Bcrypt
from unboxit.resources.errors import errors
from flask_mail import Mail, Message
if os.path.exists("env.py"):
    import env

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    'host': os.environ.get("MONGO_URI"),
}

app.secret_key = os.environ.get("SECRET_KEY")
app.config['MAIL_SERVER'] = 'smtp.sendgrid.net'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'apikey'
app.config['MAIL_PASSWORD'] = "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"
app.config['MAIL_DEFAULT_SENDER'] = "contact@tsantos.dev"
mail = Mail(app)

def page_not_found(e):
  return render_template('components/error_404.html'), 404

def internal_error(e):
  return render_template('components/error_500.html'), 500

app.register_error_handler(404, page_not_found)
app.register_error_handler(500, internal_error)

from unboxit.resources.routes import initialize_routes

api = Api(app, errors=errors)
bcrypt = Bcrypt(app)

initialize_jwt(app)
initialize_db(app)
initialize_routes(api)
initialize_cache(app)

# def test_connection():
#     with app.app_context():
#         msg = Message('Twilio SendGrid Test Email', recipients=['thiagocroza@hotmail.com'])
#         msg.body = 'This is a test email!'
#         msg.html = '<p>This is a test email!</p>'
#         mail.send(msg)
#         #test code


