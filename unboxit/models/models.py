from enum import unique
from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash


class Movie(db.Document):
    poster = db.StringField()
    media_type = db.StringField()
    title = db.StringField()
    description = db.StringField()
    year = db.StringField()
    release_date = db.StringField()
    imdb_id = db.StringField(unique=True)
    imdb_rating = db.StringField()
    vote_count = db.StringField()
    popularity = db.StringField()
    youtube_trailer_key = db.StringField()
    review = db.StringField()
    runtime = db.IntField()
    stars = db.ListField(db.StringField() )
    directors = db.ListField(db.StringField() )
    creators = db.ListField(db.StringField() )
    added_by = db.ReferenceField('User', unique_with="imdb_id")


class TvSeries(db.Document):
    poster = db.StringField()
    media_type = db.StringField()
    title = db.StringField()
    description = db.StringField()
    year = db.StringField()
    release_date = db.StringField()
    imdb_id = db.StringField(unique=True)
    imbd_rating = db.StringField()
    vote_count = db.StringField()
    popularity = db.StringField()
    youtube_trailer_key = db.StringField()
    runtime = db.IntField()
    stars = db.ListField(db.StringField() )
    creators = db.ListField(db.StringField() )
    added_by = db.ReferenceField('User', unique_with="imdb_id")


class User(db.Document):
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.EmailField(unique=True)
    username = db.StringField(required=True)
    password = db.StringField(required=True)
    movies = db.ListField(db.ReferenceField(
        'Movie', reverse_delete_rule=db.PULL))
    tv_series = db.ListField(db.ReferenceField(
        'TvSeries', reverse_delete_rule=db.PULL))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)


User.register_delete_rule(Movie, 'added_by', db.CASCADE)
