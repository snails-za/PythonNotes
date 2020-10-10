from flask import Flask


app = Flask(__name__)   #  创建Flask程序实例


@app.route("/greet/<string:name>/")
def greet_view(name):
    return "<h3>glad to meet you,<span style='color:blue'>" + name + "<span></h3>"


@app.route("/hi/<int:age>/")   # 将捕获的age参数转换为int类型
def hi_view(age):
    age += 2
    return "两年后，我" + str(age) + "岁了"


@app.route("/student/<float:score>/")
def student_view(score):
    return "我考了" + str(score) +"分"


@app.route("/welcome/<path:info>/")
def welcome_view(info):
    return "接收到的info是：" + info


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8888,debug=True)