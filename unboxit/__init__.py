import os
from flask_pymongo import PyMongo
from flask import Flask
if os.path.exists("env.py"):
    import env


app = Flask(__name__)


app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


mongo = PyMongo(app)


from unboxit import routes