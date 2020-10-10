import redis
from flask import Flask
from CookieSessionApp.views import blue1,blue2
from flask_session import Session
from datetime import timedelta


def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "abcdef"   # 设置秘钥
    app.config["SESSION_TYPE"] = "redis"  # 设置session的存储位置
    app.config["SESSION_REDIS"] = redis.Redis(host="localhost",port=6379,db=3)  # 关联操作Redis的实例对象
    app.config["SESSION_KEY_PREFIX"] = "python1905"  # 前缀配置
    app.config["PERMANENT_SESSION_LIFETIME"] = timedelta(seconds=30)  #  设置最大不交互时间
    app.register_blueprint(blue1)
    app.register_blueprint(blue2)
    Session(app)   # Flask-Session插件中的Session对象与Flask程序实例进行关联
    return app