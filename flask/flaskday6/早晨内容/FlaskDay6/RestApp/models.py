from RestApp.ext import db


class Toy(db.Model):   # 玩具模型
    __tablename__ = "toys"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),nullable=False)
    price = db.Column(db.Float,nullable=False)