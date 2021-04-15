from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class WatchList(db.Document):
    user_id = db.StringField(required=True)
    imdb = db.ListField(db.StringField(unique=True),unique=True)
class User(db.Document):
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)