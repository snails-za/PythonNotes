from HomeworkApp.ext import db


class School(db.Model):
    __tablename__ = "schools"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20),nullable=False)
    address = db.Column(db.String(30),nullable=False)
    students = db.relationship("Student",backref="sch")


class Student(db.Model):
    __tablename__ = "students"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(20), nullable=False)
    score = db.Column(db.Float,nullable=False)
    school_id = db.Column(db.Integer,db.ForeignKey("schools.id"))
