from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/obj/")
def jsonobj_view():
    data = {
        "name":"tom",
        "age":20,
        "score":93.5
    }
    return jsonify(data)


@app.route("/array/")
def jsonarray_view():
    stu1 = {"name":"tom","age":20,"score":80}
    stu2 = {"name":"alice","age":22,"score":83}
    stu3 = {"name":"jonda","age":25, "score":79}
    students = [stu1,stu2,stu3]
    return jsonify(students)