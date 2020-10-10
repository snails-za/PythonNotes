from flask_restful import Resource, fields, marshal_with, marshal
from flask_restful.reqparse import RequestParser

from HomeworkApp.models import *

rp = RequestParser()
rp.add_argument("student_name", required=True, help="必须输入student_name参数！")
rp.add_argument("student_score", required=True, help="必须输入student_score参数！")
rp.add_argument("school_id")


student_output_instance = {
    "student_id": fields.Integer(attribute="id"),
    "student_name": fields.String(attribute="name"),
    "student_score": fields.String(attribute="score"),
    "school_id":fields.Integer(default=-1)
}

student_output = {
    "code": fields.String,
    "msg": fields.String,
    "student": fields.Nested(student_output_instance)
}


class StudentResource(Resource):

    @marshal_with(student_output)
    def post(self):
        args = rp.parse_args()  # 解析参数，并且进行数据校验
        student_name = args.get("student_name")
        student_score = args.get("student_score")
        school_id = args.get("school_id")
        new_student = Student(name=student_name, score=student_score,school_id=school_id)
        db.session.add(new_student)
        db.session.commit()
        data = {
            "code": "201",
            "msg": "新生创建成功",
            "student": new_student
        }
        return data

    def get(self,stuid):
        student = Student.query.get(stuid)
        if student:
            data = {
                "code": "200",
                "msg": "查询成功",
                "student": student
            }
            return marshal(data,student_output)
        else:
            return {"code":"404","msg":"没有该生！"}


    def put(self):
        rp.add_argument("stuid",required=True,help="必须输入学号")  # 添加stuid参数
        args = rp.parse_args()
        rp.remove_argument("stuid")  # 移除stuid参数
        stuid = args.get("stuid")
        student_name = args.get("student_name")
        student_score = args.get("student_score")
        school_id = args.get("school_id")
        student = Student.query.get(stuid)
        if student:
            student.name = student_name
            student.score = student_score
            student.school_id = school_id
            db.session.commit()
            data = {
                "code": "666",
                "msg": "修改成功",
                "student": student
            }
            return marshal(data, student_output)
        else:
            return {"code": "408", "msg": "没有该生,修改失败！"}

    def delete(self,stuid):
        student = Student.query.get(stuid)
        if student:
            db.session.delete(student)
            db.session.commit()
            data = {
                "code": "205",
                "msg": "删除成功",
                "student": student
            }
            return marshal(data, student_output)
        else:
            return {"code": "409", "msg": "没有该生，删除失败！"}

