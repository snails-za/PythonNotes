from flask import Flask

from ClientApp.views import blue


def create_app():
    app = Flask(__name__)
    app.register_blueprint(blue)
    return app