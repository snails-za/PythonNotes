import redis
from flask import Flask
from flask_session import Session

from FlashApp.views import blue


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "abcdef"
    app.config["SESSION_TYPE"] = "redis"
    app.config["SESSION_REDIS"] = redis.Redis(host="localhost",port=6379,db=3)
    app.config["SESSION_KEY_PREFIX"] = "python1905"
    app.register_blueprint(blue)
    Session(app)
    return app