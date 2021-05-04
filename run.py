import os
from unboxit import app


if __name__ == '__main__':
    if os.environ.get('ENV') == "production":
        app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')))
    else:
        app.run()
