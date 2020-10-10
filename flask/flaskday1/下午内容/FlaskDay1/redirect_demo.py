from flask import Flask, redirect, jsonify
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


@app.route("/hi/")
def hi_view():
    return redirect("http://www.sohu.com")   #  重定向到外网，通过响应头Location实现重定向


@app.route("/hello/<name>/")
def hello_view(name):
    print("hello_view()......")
    return redirect("/grace/"+name+"/")   # 重定向到自己注册的路由


@app.route("/grace/<nickname>/")
def grace_view(nickname):
    print("grace_view()......")
    return "<h3 style='color:green'>you are so graceful~~~," + nickname + "</h3>"


if __name__ == '__main__':
    manager.run()