from flask import Flask
from HomeworkApp.ext import init_ext
from HomeworkApp.middleware import load_middleware
from HomeworkApp.views import c, blue

cache_config = {
    'CACHE_TYPE':'redis',
    # REDIS所在的主机
    'CACHE_REDIS_HOST':'localhost',
    'CACHE_REDIS_PORT':6379,    # Redis端口
    'CACHE_REDIS_DB':3,   # Redis数据库索引
}

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = "abcdef"
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/mydb?charset=utf8"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    init_ext(app)
    app.register_blueprint(blue)
    c.init_app(app,config=cache_config)
    load_middleware(app)
    return app