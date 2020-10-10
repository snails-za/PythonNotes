from flask import Blueprint, make_response, request

blue1 = Blueprint("cookieblue",__name__)


@blue1.route("/addcookie/")
def addcookie_view():
    r = make_response("<h3>Cookie创建成功！</h3>")
    r.set_cookie("fruit","apple")   #  如果没有设置保存时间，则浏览器关闭，该Cookie消失
    r.set_cookie("sport","Football",max_age=60)   # 保存时间为60秒
    return r


@blue1.route("/delcookie/<name>/")
def delete_cookie(name):
    r = make_response("<h3>名称为" + name + "的Cookie被删除！</h3>")
    r.delete_cookie(name)   # 删除指定名称的Cookie
    return r


@blue1.route("/cookie/<name>/")
def cookie_view(name):
    cookie_value = request.cookies.get(name,"无此Cookie")  # 根据Cookie名称查看单个Cookie
    return "该Cookie的值为：" + cookie_value


@blue1.route("/cookies/")
def show_cookies():
    cookies = request.cookies   # 获取所有Cookie
    html = ""
    for k,v in cookies.items():   # 遍历所有Cookie
        html += k
        html += "============>"
        html += v
        html += "<br/>"
    return html