from flask_restful import Resource
from flask_restful.reqparse import RequestParser

rp2 = RequestParser()
rp2.add_argument("hobby",required=True,action="append")  # 可以接收多个同名参数hobby,接收的参数以列表形式返回
rp2.add_argument("name",location="args")  # 接收查询字符串参数中的信息

rp3 = RequestParser()
rp3.add_argument("User-Agent",location="headers")  # 接收请求头中的信息
rp3.add_argument("food",location="cookies")  # 接收Cookie名称为food的cookie值



class OtherResource(Resource):

    def post(self):
        args = rp2.parse_args()
        hobby = args.get("hobby")
        name = args.get("name")
        print("接收到的hobby是：",hobby,"name=",name)
        data = {
            "code":"666",
            "msg":"请查看控制台~~~"
        }
        return data

    def get(self):
        print("before...")
        args = rp3.parse_args()
        print("after...")
        ua = args.get("User-Agent")
        food = args.get("food")
        print("ua=",ua,"food=",food)
        data = {
            "code": "888",
            "msg": "请查看控制台~~~"
        }
        return data