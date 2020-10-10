from flask import Flask, render_template

app = Flask(__name__)   # 创建Flask程序实例

options = {
    "endpoint": "wel",
    "methods": ["GET"]
}

@app.route("/wel/<name>/", **options)
def welcome_view(name):
    resp = {
        "nickname": name
    }
    return render_template("hello/welcome.html", **resp)   #   根据模板位置，渲染模板


@app.route("/student/<int:score>/")
def student_view(score):
    return render_template("tags/if_tag.html",stuscore=score)


@app.route("/fruits/")
def fruits_view():
    fruits = ["苹果","香蕉","菠萝","橙子"]
    return render_template("tags/for_tag.html",fruits=fruits)


@app.route("/child/")
def child_view():
    return render_template("extends/child.html",info="秦始皇")


@app.route("/filter/")
def filter_view():
    s = "heLLo worLD"
    nums = [1,2,3,4,5]
    danger = "<script>alert('大笨蛋！')</script>"
    return render_template("filter/filter_demo.html",**locals())


@app.route("/macro/")
def macro_view():
    sports = ["足球","跑步","台球","乒乓球"]
    return render_template("macro/use.html",**locals())
