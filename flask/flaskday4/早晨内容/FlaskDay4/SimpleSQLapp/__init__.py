from flask import Flask

from SimpleSQLapp.ext import init_ext


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@localhost:3306/mydb?charset=utf8"  # 连接配置
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False  # 压制警告
    init_ext(app)
    return app