from flask import Flask

from ConfigApp.views import blue


def create_app():
    app = Flask(__name__)
    app.config["HERO"] = "1900"
    app.register_blueprint(blue)
    return app
