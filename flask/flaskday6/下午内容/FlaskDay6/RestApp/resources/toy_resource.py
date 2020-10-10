from flask import request
from flask_restful import Resource, fields, marshal_with, marshal

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

# 多个玩具输出格式
output_toys = {
    "code":fields.String,
    "msg":fields.String,
    #"toys":fields.List(fields.Nested(toy_instance_output))
    "toys":fields.Nested(toy_instance_output)
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

    def get(self,toy_id):
        toy = Toy.query.get(toy_id)
        if toy:
            data = {
                "code":"678",
                "msg":"查询成功！",
                "toy":toy
            }
            return marshal(data,output_toy)  # 将原始数据data与output_toy输出模板进行比对
        else:
            data = {
                "code":"999",
                "msg":"无此玩具！"
            }
            return data


class ToysResource(Resource):    # 另一个玩具资源类

    def get(self):
        toys = Toy.query.all()
        data = {
            "code":"200",
            "msg":"所有玩具查询完毕！",
            "toys":toys
        }
        return marshal(data,output_toys)