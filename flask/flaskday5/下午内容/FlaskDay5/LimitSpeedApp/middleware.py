import redis
from flask import request, g

r = redis.Redis(host="localhost",port=6379,db=3)  # 使用该对象操作Redis


def load_middleware(app):

    @app.before_request   # 每次接到请求都会执行
    def a():
        ip = request.remote_addr   # 获取发送请求的客户端的IP地址
        key = "limit:" + ip
        is_ok = r.set(key,1,ex=60,nx=True)  # 当key不存在时，set命令才能执行成功，过期时间为60秒
        print("is_ok=",is_ok)
        if is_ok or r.incr(key) <= 5:
            g.visit_count = r.get(key).decode()   #  获取当前访问次数，并赋值给g对象的visit_count属性
        else:
            return "<h3 style='color:red'>访问次数过于频繁，请稍后再访问！</h3>"