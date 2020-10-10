from flask import Blueprint, render_template

blue = Blueprint("myblue",__name__)


@blue.route("/index/")
def index_view():
    return render_template("index.html")