from flask import Blueprint,session


blue2 = Blueprint("sessionblue",__name__)


@blue2.route("/addsession/")
def session_view():
    session["username"] = "tom"    # 设置session属性
    session["password"] = "123456"
    return "<h3>Session属性添加成功</h3>"


@blue2.route("/session/<name>/")
def get_session(name):
    data = session.get(name,"session的该属性名不存在！")   # 查询session
    return data


@blue2.route("/popsession/<name>/")
def pop_session(name):
    data = session.pop(name,"session的该属性名不存在！")
    return data


@blue2.route("/clear/")
def clear_session():
    session.clear()
    return "清空session！"


@blue2.route("/sessions/")
def sessions_view():
    html = ""
    for k,v in session.items():   #  遍历当前session的属性名、属性值
        html += k
        html += "==========>"
        html += str(v)
        html += "<br/>"
    return html