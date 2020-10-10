from flask_restful import Api

from HomeworkApp.resources.school_resource import SchoolResource
from HomeworkApp.resources.student_resource import StudentResource

api = Api()


def init_api(app):
    api.init_app(app)


api.add_resource(SchoolResource,"/school/")
api.add_resource(StudentResource,"/student/","/student/<stuid>/")