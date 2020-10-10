from flask import Blueprint, request, render_template, session, redirect, url_for, flash

blue = Blueprint("myblue",__name__)


@blue.route("/login/",methods=["GET","POST"])
def login_view():
    if request.method == "GET":
        return render_template("login.html")   # 加载登录模板
    elif request.method == "POST":
        logname = request.form.get("logname")  # 获取请求体中的参数
        logpwd = request.form.get("logpwd")  # 获取请求体中的参数
        if logname == "tom" and logpwd == "123456":
            session["username"] = logname  # 如果登录验证成功，则添加一个session属性
            return redirect(url_for("myblue.welcome_view"))   # 重定向到欢迎页面
        else:   # 如果验证失败
            flash("用户名或密码错误，请重新输入！")   # flash将信息存储于session中
            flash("认真点！")
            return redirect(url_for("myblue.login_view"))   # 重定向到登录页面


@blue.route("/wel/")
def welcome_view():
    return render_template("welcome.html")


@blue.route("/logout/")
def logout_view():
    session.clear()  # 删除session信息
    return redirect(url_for("myblue.login_view"))  # 重定向到登录页面