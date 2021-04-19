from enum import unique
from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash
class Movie(db.Document):
    title = db.StringField(required=True)
    description = db.StringField(required=True)
    year = db.StringField(required=True)
    release_date = db.StringField(required=True)
    imdb_id = db.StringField(required=True)
    imdb_rating = db.StringField(required=True)
    vote_count = db.StringField(required=True)
    popularity = db.StringField(required=True)
    youtube_trailer_key = db.StringField(required=True)
    runtime = db.IntField(required=True)
    rated = db.StringField(required=True)
    genres = db.ListField(db.StringField(), required=True)
    stars = db.ListField(db.StringField(), required=True)
    directors = db.ListField(db.StringField(), required=True)
    countries = db.ListField(db.StringField(), required=True)
    language = db.ListField(db.StringField(), required=True)
    added_by = db.ReferenceField('User', unique_with="imdb_id")


class TvSeries(db.Document):
    title = db.StringField(required=True)
    description = db.StringField(required=True)
    year = db.StringField(required=True)
    release_date = db.StringField(required=True)
    imdb_id = db.StringField(required=True)
    imbd_rating = db.StringField(required=True)
    vote_count = db.StringField(required=True)
    popularity = db.StringField(required=True)
    youtube_trailer_key = db.StringField(required=True)
    runtime = db.IntField(required=True)
    stars = db.ListField(db.StringField(), required=True)
    creators = db.ListField(db.StringField(), required=True)
    countries = db.ListField(db.StringField(), required=True)
    language = db.ListField(db.StringField(), required=True)
    production_companies = db.ListField(db.StringField(), required=True)
    networks = db.ListField(db.StringField(), required=True)
    added_by = db.ReferenceField('User')


class User(db.Document):
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.EmailField(required=True, unique=True)
    username = db.StringField(required=True)
    password = db.StringField(required=True)
    movies = db.ListField(db.ReferenceField('Movie', reverse_delete_rule=db.PULL))
    tv_series = db.ListField(db.ReferenceField('TvSeries', reverse_delete_rule=db.PULL))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)