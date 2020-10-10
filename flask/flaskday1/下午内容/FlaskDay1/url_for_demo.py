from flask import Flask, redirect, url_for
from flask_script import Manager


app = Flask(__name__)
manager = Manager(app)


@app.route("/hello/<name>/")
def hello_view(name):
    ok_url = url_for(endpoint="w",nickname=name)   #  通过url_for()的第一个参数为endpoint,指向的是视图函数路由，后面关键字参数名与路由捕获参数名保持一致
    print("ok_url=",ok_url)
    return redirect(ok_url)  # 重定向

@app.route("/wel/<nickname>/", endpoint="w")
def welcome_view(nickname):
    return "<h3>Welcome,<span style='color:blue'>" + nickname + "</span></h3>"

a = app.url_map
print(a)

if __name__ == '__main__':
    manager.run()