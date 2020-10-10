from flask import Blueprint


sport_blue = Blueprint("sportblue",__name__)


@sport_blue.route("/jog/")
def jog_view():
    return "<h3 style='color:pink'>慢跑运动......</h3>"


@sport_blue.route("/ball/")
def ball_view():
    return "<h3 style='color:blue'>打球中~~~~~~</h3>"