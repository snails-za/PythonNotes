from flask import Blueprint


food_blue = Blueprint("foodblue",__name__)  # 创建蓝图对象，指定蓝图名称和导入名称


@food_blue.route("/noodles/")
def noodles_view():
    return "<h3 style='color:green'>吃面条~~~~~~</h3>"


@food_blue.route("/rice/")
def rice_view():
    return "<h3 style='color:yellow'>吃米饭......</h3>"