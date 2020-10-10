from flask import Blueprint, request

blue = Blueprint("myblue",__name__)


@blue.route("/args/",methods=["GET","POST"])
def args_view():
    name = request.args.get("stuname","没有stuname参数")   # 接收查询字符串参数,参数名为stuname
    age = request.args.get("stuage","没有stuage参数")  # 接收查询字符串参数,参数名为stuage
    return "姓名为：" + name + "；年龄为：" + age


@blue.route("/form/",methods=["POST"])
def form_view():
    name = request.form.get("stuname", "没有stuname参数")  # 接收请求体中的参数,参数名为stuname
    age = request.form.get("stuage", "没有stuage参数")  # 接收请求体中的参数,参数名为stuage
    return "姓名为：" + name + "；年龄为：" + age