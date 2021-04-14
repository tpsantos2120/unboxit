from .db import db


class User(db.Document):
    first_name = db.StringField(required=True)
    last_name = db.StringField(required=True)
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    movies = db.ListField(db.ReferenceField('Movies'), required=True)
    tv_series = db.ListField(db.ReferenceField('TvSeries'), required=True)


class Movie(db.Document):
    title = db.StringField(required=True)
    description = db.StringField(required=True)
    year = db.StringField(required=True)
    release_date = db.StringField(required=True)
    imdb_id = db.StringField(required=True, unique=True)
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


class TvSeries(db.Document):
    title = db.StringField(required=True)
    description = db.StringField(required=True)
    year = db.StringField(required=True)
    release_date = db.StringField(required=True)
    imdb_id = db.StringField(required=True, unique=True)
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