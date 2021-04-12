import json
from bson import ObjectId
from unboxit import app, mongo

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


@app.route("/")
def home():
    return test_db_connection()


def test_db_connection():
    existing_user = mongo.db.users.find_one(
            {"username": "thiago"})
    user = JSONEncoder().encode(existing_user)
    return user

