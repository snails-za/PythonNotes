from flask import Flask
from BlueprintApp.views import food_blue,sport_blue


def create_app():
    app = Flask(__name__)    # 创建Flask程序实例
    app.register_blueprint(food_blue)  # 关联food_blue蓝图
    app.register_blueprint(sport_blue)  #  关联sport_blue蓝图
    return app