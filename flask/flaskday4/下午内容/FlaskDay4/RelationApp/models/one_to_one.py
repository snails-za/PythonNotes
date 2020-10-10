from RelationApp.ext import db
print("one_to_one,db=",id(id))


class Person(db.Model):    # 被依赖的一方
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    sex = db.Column(db.String(10),nullable=False)
    c = db.relationship("Card",backref="per",uselist=False)   # uselist=False 禁用列表


class Card(db.Model):   # 依赖的一方
    __tablename__ = "cards"
    cardno = db.Column(db.String(20),primary_key=True)   # 卡号
    color = db.Column(db.String(20),nullable=False)
    person_id = db.Column(db.Integer,db.ForeignKey("person.id"),unique=True)  # 唯一外键