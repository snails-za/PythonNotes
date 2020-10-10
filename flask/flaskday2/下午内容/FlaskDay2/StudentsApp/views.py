from flask import Flask, render_template

from StudentsApp.db_tools import *

app = Flask(__name__)


@app.route("/students/")
def students_all_view():
    students = select_allstudents()
    return render_template("students.html",students=students)


@app.route("/student/<int:id>/")
def student_detail_view(id):
    student = select_detail_student(id)
    return render_template("student_detail.html",student=student)
