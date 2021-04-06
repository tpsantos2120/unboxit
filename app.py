import os
from flask_pymongo import PyMongo
from flask import Flask
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


mongo = PyMongo(app)


@app.route("/")
def home():
    test_db_connection()
    return "test_db_connection() worked!"


def test_db_connection():
    existing_user = mongo.db.users.find_one(
            {"username": "thiago"})
    print(existing_user)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=os.environ.get("DEBUG"))

