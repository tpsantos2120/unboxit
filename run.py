import os
from unboxit.app import app

if __name__ == '__main__':
    if os.environ.get('ENV_STATE') == "production":
        #app.config["ENV"] = "production"
        app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')))
    elif os.environ.get('ENV_STATE') == "development":
        app.config["ENV"] = "development"
        app.run(debug=os.environ.get("DEBUG"))