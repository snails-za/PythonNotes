from flask import Flask
from flask_script import Manager


app = Flask(__name__)   # 创建Flask程序实例
manager = Manager(app)    # Manager对象与Flask程序实例进行关联


@app.route("/nice/", methods=["GET"])
def nice_view():
    return "<h3 style='color:blue'>You are so nice~~~</h3>"


@manager.command   # 使用该装饰器注册一个命令
def mycommand():
    return "this is my command......"


@manager.command    # 注册一个命令，函数接收的参数在命令行中动态传入
def callsb(tel,greet):
    print("拨打电话：",tel,"；问候语：",greet)
    return "通话成功~~~"



if __name__ == '__main__':
    manager.run()   # 通过Flask-Script插件的Manager对象进行启动服务