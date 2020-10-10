from flask import Blueprint, g

blue = Blueprint("myblue",__name__)


@blue.route("/index/")
def index_view():
    count = g.visit_count
    return "<h3>这是第" + str(count) + "次访问~~~</h3>"