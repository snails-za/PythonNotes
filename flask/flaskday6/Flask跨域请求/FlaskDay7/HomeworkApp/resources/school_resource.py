from flask_restful import Resource, fields, marshal_with
from flask_restful.reqparse import RequestParser

from HomeworkApp.models import *

rp = RequestParser()
rp.add_argument("school_name",required=True,help="必须输入school_name参数！")
rp.add_argument("school_address",required=True,help="必须输入school_address参数！")

school_output_instance = {
    "school_id":fields.Integer(attribute="id"),
    "school_name":fields.String(attribute="name"),
    "school_address":fields.String(attribute="address")
}

school_output = {
    "code":fields.String,
    "msg":fields.String,
    "school":fields.Nested(school_output_instance)
}

class SchoolResource(Resource):

    @marshal_with(school_output)
    def post(self):
        args = rp.parse_args()   # 解析参数，并且进行数据校验
        school_name = args.get("school_name")
        school_address = args.get("school_address")
        new_school = School(name=school_name,address=school_address)
        db.session.add(new_school)
        db.session.commit()
        data = {
            "code":"201",
            "msg":"新学校创建成功",
            "school":new_school
        }
        return data
