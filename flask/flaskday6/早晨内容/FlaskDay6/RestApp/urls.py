from flask_restful import Api

from RestApp.resources.toy_resource import ToyResource

api = Api()   # 创建Api对象，靠该对象关联资源类与路由


def init_api(app):
    api.init_app(app)   # Api对象与Flask程序实例关联

api.add_resource(ToyResource,"/toy/")    # 关联资源类与路由