from flask import session, request, flash, render_template
from unboxit import app, mongo
import jwt
from unboxit.json_encoder import JSONEncoder
from werkzeug.security import generate_password_hash


users = mongo.db.users
JWT_ALGORITHM = "HS256"


@app.route("/")
def home():
    return render_template('/views/home.html', title='Home')



@app.route("/api/users", methods=['GET', 'POST'])
def register_user():

    if request.method == "POST":
        if 'username' in session:
            flash('You are already registered!')
            return "You are already registered!"
        user_exist = users.find_one({'username': 'noxx'})
        if user_exist:
            flash('User Exist.')
            return "User Exist."
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
            flash('You have been successfully registered.')
            return "You have been successfully registered."
    return "Nothing"
