from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash


class Watchlist(db.Document):
    poster = db.StringField(required=True)
    media_type = db.StringField(required=True)
    title = db.StringField(required=True)
    description = db.StringField(required=True)
    year = db.StringField(required=True)
    release_date = db.StringField(required=True)
    imdb_id = db.StringField(required=True)
    imdb_rating = db.StringField(required=True)
    vote_count = db.StringField(required=True)
    popularity = db.StringField(required=True)
    youtube_trailer_key = db.StringField(required=True)
    review = db.StringField(required=True)
    runtime = db.IntField(required=True)
    stars = db.ListField(db.StringField(), required=True)
    directors = db.ListField(db.StringField())
    creators = db.ListField(db.StringField())
    added_by = db.ReferenceField('User', unique_with="imdb_id")


class User(db.Document):
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.EmailField(unique=True, required=True)
    username = db.StringField(required=True)
    password = db.StringField(required=True)
    watchlists = db.ListField(db.ReferenceField(
        'Watchlist', reverse_delete_rule=db.PULL))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


User.register_delete_rule(Watchlist, 'added_by', db.CASCADE)
