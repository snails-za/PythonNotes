import time

from flask import Blueprint, render_template, request, session, redirect, url_for, flash
from flask_cache import Cache

from HomeworkApp.models import Student, User

blue = Blueprint("myblue",__name__)
c = Cache()


@blue.route("/student/<int:stuid>/")
@c.cached(timeout=30)
def student_view(stuid):
    print("正在耗时查询数据库......")
    time.sleep(3)
    student = Student.query.get(stuid)
    if student:
        return render_template("student.html",student=student)
    else:
        return "<h3 style='color:red'>没有学号为" + str(stuid) + "的学生</h3>"


@blue.route("/login/",methods=["GET","POST"])
def login_view():
    if request.method == "GET":
        return render_template("login.html")
    elif request.method == "POST":
        logname = request.form.get("logname")
        logpwd = request.form.get("logpwd")
        user = User.query.filter_by(username=logname,password=logpwd).first()
        if user:
            session["username"] = logname   # 登录验证成功，则在session中添加一个username属性
            return redirect(url_for("myblue.success_view"))
        else:
            flash("用户名或密码错误！")
            return redirect(url_for("myblue.login_view"))


@blue.route("/success/")
def success_view():
    return render_template("success.html")