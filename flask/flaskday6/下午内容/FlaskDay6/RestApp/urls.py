from flask_restful import Api

from RestApp.resources.cake_resource import CakeResource
from RestApp.resources.other_resource import OtherResource
from RestApp.resources.toy_resource import ToyResource,ToysResource

api = Api()   # 创建Api对象，靠该对象关联资源类与路由


def init_api(app):
    api.init_app(app)   # Api对象与Flask程序实例关联


api.add_resource(ToyResource,"/toy/","/toy/<toy_id>/")    # 关联ToyResource资源类与路由
api.add_resource(ToysResource,"/toys/")  # 关联ToysResource资源类与路由

api.add_resource(CakeResource,"/cake/")  # 关联CakeResource资源类与路由

api.add_resource(OtherResource,"/other/") # 关联OtherResource资源类与路由