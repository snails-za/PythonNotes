from flask import Flask, render_template, jsonify

from AjaxApp.db_tools import regname_is_exists

app = Flask(__name__)


@app.route("/register/")
def register_view():
    return render_template("reg/register.html")


@app.route("/check/<username>/")
def checkname_view(username):
    is_exists = regname_is_exists(username)
    if is_exists:   # 如果该注册名在数据库中已存在
        data = {
            "code":"555",
            "msg":"sorry,该用户名已存在，请重新选择注册用户名！"
        }
    else:   # 如果不存在
        data = {
            "code":"666",
            "msg":"恭喜，该用户名可以注册~~~"
        }

    return jsonify(data)
