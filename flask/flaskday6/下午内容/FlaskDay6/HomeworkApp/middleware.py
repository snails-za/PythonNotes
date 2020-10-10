from flask import request, session, flash, redirect, url_for

REQUIRED_LOGIN = ["/success/"]   # 需要登录验证的路由


def load_middleware(app):

    @app.before_request
    def a():
        current_path = request.path  # 获取当前访问的路由
        print("current_path=",current_path)
        if current_path in REQUIRED_LOGIN:
            username = session.get("username")
            if username is None:
                flash("您还未登录，不能直接访问成功页面！")
                return redirect(url_for("myblue.login_view"))
