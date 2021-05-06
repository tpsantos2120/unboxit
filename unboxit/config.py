import os
from dotenv import load_dotenv


class Config(object):
    """
        Load generic environment variables which are extended by 
        one of the server environments below.
    """
    load_dotenv()
    ENV = os.environ.get('ENV')
    IMDB_API_HOST = os.environ.get('IMDB_API_HOST')
    IMDB_BASE_URL = os.environ.get('IMDB_BASE_URL')
    IMDB_SECRET_KEY = os.environ.get('IMDB_SECRET_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    MONGODB_SETTINGS = {
        'host': os.environ.get('MONGODB_PRODUCTION')
    }
    MONGO_DBNAME = os.environ.get('MONGO_DBNAME')
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'apikey'
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')


class ProductionConfig(Config):
    """
        Override Environment Variables for production.
    """
    DEBUG = False
    TESTING = False
    FLASK_ENV = "production"
    IP = os.environ.get('IP')
    PORT = os.environ.get('PORT')


class DevelopmentConfig(Config):
    """
        Override Environment Variables for development.
    """
    DEBUG = True
    MONGODB_SETTINGS = {
        'host': os.environ.get('MONGODB_DEVELOPMENT')
    }


class TestingConfig(Config):
    """
        Override Environment Variables for testing.
    """
    load_dotenv()
    TESTING = True
    MONGODB_SETTINGS = {
        'host': os.environ.get('MONGODB_TESTING')
    }
