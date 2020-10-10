from flask import Blueprint, g

blue = Blueprint("myblue",__name__)


@blue.route("/index/")
def index_view():
    try:
        5 / 0
    except:
        pass
    return "<h3 style='color:green'>Index,Nice to meet you~~~," + g.book + "</h3>"