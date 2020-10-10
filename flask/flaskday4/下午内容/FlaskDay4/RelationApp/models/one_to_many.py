from RelationApp.ext import db
print("one_to_many,db=",id(id))


class School(db.Model):    # "一方"模型
    __tablename__ = "schools"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),nullable=False)
    address = db.Column(db.String(30),nullable=False)
    students = db.relationship("Student",backref="sch")   #  在“一”方模型中通过relationship函数从对象角度关联"多"方


class Student(db.Model):    #  "多方"模型
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    score = db.Column(db.Float,nullable=False)
    school_id = db.Column(db.Integer,db.ForeignKey("schools.id"),nullable=False)  # 在“多”方模型中通过在Column()中设置ForeignKey()从数据库表角度设置外键，关联“一”方
