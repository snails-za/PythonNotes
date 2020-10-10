from flask import Flask, make_response, redirect

app = Flask(__name__) #  创建Flask程序实例


@app.route("/student/<name>/<int:score>/")
def student_view(name,score):
    s = "我叫" + name + "；考了" + str(score) + "分"
    r = make_response(s)
    return r


@app.route("/vip/<name>/<path:info>/<home>/")
def vip_view(name,info,home):
    return "接收到的info参数是：" + info


@app.route("/nice/<name>/")
def nice_view(name):
    return redirect("http://httpbin.org/get?nickname="+name)
