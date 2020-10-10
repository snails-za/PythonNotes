from flask import Blueprint, current_app, render_template

blue = Blueprint("myblue",__name__)


@blue.route("/index/")
def index_view():
    appconfig = current_app.config   # 获取当前程序实例的所有配置
    appconfig["DEBUG"] = False   # 在代码中动态地修改程序实例的配置
    html = ""
    for k,v in appconfig.items():
        html += k
        html += "==========>"
        html += str(v)
        html += "<br/>"
    return html


@blue.route("/nice/")
def nice_view():
    5 / 0
    return "nice~~~"


@blue.route("/allconfig/")
def config_view():
    return render_template("show_config.html")


