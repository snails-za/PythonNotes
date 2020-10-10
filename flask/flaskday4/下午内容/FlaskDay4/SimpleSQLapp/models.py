from SimpleSQLapp.ext import db


class Product(db.Model):   # 继承Model类，为模型类
    __tablename__ = "products"  # 对应的数据库表名称
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)  # 主键自增
    name = db.Column(db.String(20),nullable=False)
    price = db.Column(db.Float,nullable=False)
    address = db.Column(db.String(30))
    brand = db.Column(db.String(20),nullable=False)