from flask import Flask
from flask_cors import CORS

from ServerApp.views import blue


def create_app():
    app = Flask(__name__)
    app.register_blueprint(blue)
    CORS(app,supports_credentials=True)   # 允许其他网站跨域请求
    return app