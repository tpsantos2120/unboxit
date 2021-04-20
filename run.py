import os
from unboxit import app
from gevent.pywsgi import WSGIServer


if __name__ == '__main__':
    if os.environ.get('ENV_STATE') == "production":
        app.config["ENV"] = "production"
        # app.run(host=os.environ.get('IP'),
        #     port=int(os.environ.get('PORT')))
        http_server = WSGIServer(('0.0.0.0', 5000), app)
        http_server.serve_forever()
    elif os.environ.get('ENV_STATE') == "development":
        app.config["ENV"] = "development"
        app.run(debug=os.environ.get("DEBUG"))