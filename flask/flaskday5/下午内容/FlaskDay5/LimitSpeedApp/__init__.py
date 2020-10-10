from flask import Flask

from LimitSpeedApp.middleware import load_middleware
from LimitSpeedApp.views import blue


def create_app():
    app = Flask(__name__)
    app.register_blueprint(blue)
    load_middleware(app)
    return app