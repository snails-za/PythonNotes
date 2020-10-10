from flask import Blueprint, make_response

blue = Blueprint("myblue",__name__)


@blue.route("/cookie/")
def cookie_view():
    response = make_response("Cookie添加成功！")
    response.set_cookie("food","noodles")
    return response