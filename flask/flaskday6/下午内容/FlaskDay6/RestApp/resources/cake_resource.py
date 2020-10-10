from flask_restful import Resource, marshal_with, fields
from flask_restful.reqparse import RequestParser

from RestApp.models import *

rp1 = RequestParser()  # 创建RequestParser对象
rp1.add_argument("name",required=True,type=str,help="必须传递name参数！")   # 添加参数，并设置参数校验规则
rp1.add_argument("c_price",required=True,type=float,
                 help="必须传递c_price参数，而且是浮点型！",
                 dest="cake_price")  # 前端传递c_price参数，后端通过cake_price接收


cake_output_instance = {
    "cake_id":fields.Integer(attribute="id"),
    "cake_name":fields.String(attribute="name"),
    "cake_price":fields.Float(attribute="price")
}

cake_output = {
    "code":fields.String,
    "msg":fields.String,
    "cake":fields.Nested(cake_output_instance)
}


class CakeResource(Resource):

    @marshal_with(cake_output)
    def post(self):
        print("before parse_args()......")
        args = rp1.parse_args()  # 获取所有参数，并校验
        print("after parse_args()......")
        name = args.get("name")   # 接收name参数
        price = args.get("cake_price")  # 接收cake_price参数
        new_cake = Cake(name=name,price=price)
        db.session.add(new_cake)
        db.session.commit()
        data = {
            "code":"666",
            "msg":"新建蛋糕成功！",
            "cake":new_cake
        }
        return data

