from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()   #  使用该对象操作关系型数据库


def init_ext(app):
    db.init_app(app)   #  SQLAlchemy对象与Flask程序实例进行关联