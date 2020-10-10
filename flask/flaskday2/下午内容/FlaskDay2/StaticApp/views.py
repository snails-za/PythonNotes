from flask import Flask, render_template, url_for, redirect

app = Flask(__name__)


@app.route("/pic/")
def pic_view():
    return render_template("demo/show_pic.html")


# 如果需要从  模板  中通过新的endpoint获取静态资源， 需要新构建静态视图规则
app.static_folder = "static2"
if app.has_static_folder:
    app.add_url_rule(
        "/s/<path:filename>",
        endpoint="static2",
        view_func=app.send_static_file
    )

print(app.url_map)