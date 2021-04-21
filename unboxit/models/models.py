from enum import unique
from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash
class Movie(db.Document):
    title = db.StringField( null=True)
    description = db.StringField(null=True)
    year = db.StringField( null=True)
    release_date = db.StringField( null=True)
    imdb_id = db.StringField( null=True)
    imdb_rating = db.StringField( null=True)
    vote_count = db.StringField( null=True)
    popularity = db.StringField( null=True)
    youtube_trailer_key = db.StringField( null=True)
    runtime = db.IntField( null=True)
    rated = db.StringField(null=True)
    genres = db.ListField(db.StringField(),  null=True)
    stars = db.ListField(db.StringField(),  null=True)
    directors = db.ListField(db.StringField(),  null=True)
    countries = db.ListField(db.StringField(),  null=True)
    language = db.ListField(db.StringField(),  null=True)
    added_by = db.ReferenceField('User', unique_with="imdb_id")


class TvSeries(db.Document):
    title = db.StringField( null=True)
    description = db.StringField( null=True)
    year = db.StringField( null=True)
    release_date = db.StringField( null=True)
    imdb_id = db.StringField( null=True)
    imbd_rating = db.StringField( null=True)
    vote_count = db.StringField( null=True)
    popularity = db.StringField( null=True)
    youtube_trailer_key = db.StringField( null=True)
    runtime = db.IntField( null=True)
    stars = db.ListField(db.StringField(),  null=True)
    creators = db.ListField(db.StringField(),  null=True)
    countries = db.ListField(db.StringField(),  null=True)
    language = db.ListField(db.StringField(),  null=True)
    production_companies = db.ListField(db.StringField(),  null=True)
    networks = db.ListField(db.StringField(),  null=True)
    added_by = db.ReferenceField('User')


class User(db.Document):
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    email = db.EmailField( unique=True)
    username = db.StringField(required=True)
    password = db.StringField(required=True)
    movies = db.ListField(db.ReferenceField('Movie', reverse_delete_rule=db.PULL))
    tv_series = db.ListField(db.ReferenceField('TvSeries', reverse_delete_rule=db.PULL))

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    
    def check_password(self, password):
        return check_password_hash(self.password, password)