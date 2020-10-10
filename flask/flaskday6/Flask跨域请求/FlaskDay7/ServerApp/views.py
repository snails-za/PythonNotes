from flask import Blueprint, jsonify

blue = Blueprint("myblue",__name__)


@blue.route("/nice/")
def nice_view():
    data = {
        "msg":"恭喜，跨域请求成功！"
    }
    return jsonify(data)