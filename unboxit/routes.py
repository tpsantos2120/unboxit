from flask import session
from unboxit import app, mongo
from unboxit.json_encoder import JSONEncoder
from werkzeug.security import generate_password_hash

users = mongo.db.users


@app.route("/api/users", methods=['GET', 'POST'])
def register_user():
    if request.method == "POST":
    user_exist = users.find_one({'username': 'noxx'})

    if user_exist:
        return "User Exist"
    else:
        hashed_password = generate_password_hash("test")
        new_user = {
            'first_name': "Thi",
            'last_name': "ago",
            'username': "noxx",
            'password': hashed_password
        }
        users.insert_one(new_user)
        session["username"] = "Thiago"
        return "Registered"
