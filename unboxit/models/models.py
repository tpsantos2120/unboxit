from .db import db

class User(db.Document):
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)