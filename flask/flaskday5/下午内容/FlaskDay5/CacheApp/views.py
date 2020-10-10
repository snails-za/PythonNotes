import time
from flask import Blueprint
from flask_cache import Cache

blue = Blueprint("myblue",__name__)
c = Cache()   # 处理缓存数据的缓存对象

count = 0   # 用来记录访问的次数


@blue.route("/index/")
@c.cached(timeout=30,key_prefix="python1905")
def index_view():
    print("缓存中没有相应内容，模拟耗时操作......")
    time.sleep(3)
    global count
    count += 1
    return "<h3>这是第<span style='color:blue'>" + str(count) + "</span>次访问</h3>"