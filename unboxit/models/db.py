from flask_mongoengine import MongoEngine

db = MongoEngine()


def initialize_db(app):
    """
        Register db instance with app.
    """
    db.init_app(app)
