from flask import request
from flask_restful import Resource, fields, marshal_with

from RestApp.models import *

# 针对玩具实例对象输出格式
toy_instance_output = {
    "id":fields.Integer,
    "toy_name":fields.String(attribute="name"),
    "price":fields.Float
}

# 玩具输出格式
output_toy = {
    "code":fields.String,
    "msg":fields.String,
    "toy":fields.Nested(toy_instance_output)
}


class ToyResource(Resource):   # 自定义玩具资源类
    @marshal_with(output_toy)
    def post(self):   # 处理POST请求，实现资源表现层状态转换
        toy_name = request.form.get("toy_name")   # 接收请求体参数
        toy_price = request.form.get("toy_price")  # 接收请求体参数
        new_toy = Toy(name=toy_name,price=toy_price)
        db.session.add(new_toy)
        db.session.commit()  # 添加到数据库，并提交
        data = {
            "code":"666",
            "msg":"新玩具创建成功！",
            "toy":new_toy
        }
        return data
