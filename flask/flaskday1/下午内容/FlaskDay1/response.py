from flask import Flask, make_response
from flask_script import Manager


app = Flask(__name__)
manager = Manager(app)


@app.route("/bread/")
def bread_view():
    r = make_response("<h3 style='color:blue'>省委书记来了~~~</h3>")   # 创建响应对象
    r.headers["fruit"] = "banana is delicious~~~"   # 通过响应对象添加响应头信息
    r.headers["Content-Type"] = "text/plain; charset=utf-8" # 通过响应对象修改响应头信息
    return r


if __name__ == '__main__':
    manager.run()