from flask import Flask


app = Flask(__name__)  # 创建Flask程序实例对象，构造方法中传入__name__, __name__为导入名称


@app.route("/hello/")    # app.route()方法作为装饰器，装饰一个视图函数(请求处理函数)
def hello_view():
   # 5 / 0
    return "<h3 style='color:red'>Hello,欢迎学习Flask......</h3>"


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8888,debug=True)    # 通过Flask程序实例启动服务