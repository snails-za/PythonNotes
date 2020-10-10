from flask import Blueprint, request, render_template, redirect, url_for

from HomeworkApp.models import *

blue = Blueprint("myblue",__name__)


@blue.route("/addschool/",methods=["GET","POST"])
def addschool_view():
    if request.method == "GET":
        return render_template("add_school.html")
    elif request.method == "POST":
        schname = request.form.get("schname")
        schaddress = request.form.get("schaddress")
        new_school = School(name=schname,address=schaddress)
        db.session.add(new_school)
        db.session.commit()
        return redirect(url_for("myblue.addschool_view"))


@blue.route("/addstudent/",methods=["GET","POST"])
def addstudent_view():
    if request.method == "GET":
        schools = School.query.all()    # 进入添加学生页面之前，先查询所有可供选择的学校
        return render_template("add_student.html",schools=schools)
    elif request.method == "POST":
        stuname = request.form.get("stuname")
        stuscore = request.form.get("stuscore")
        sch_id = request.form.get("sch")   # 接收所选学校的ID
        new_student = Student(name=stuname,score=stuscore,school_id=sch_id)
        db.session.add(new_student)
        db.session.commit()
        return redirect(url_for("myblue.students_view"))    # 重定向到所有学生页面


@blue.route("/students/")
def students_view():
    students = Student.query.all()
    return render_template("all_students.html",students=students)

