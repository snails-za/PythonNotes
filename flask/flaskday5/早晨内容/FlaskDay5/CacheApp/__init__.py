from flask import Flask

# 缓存配置信息
from CacheApp.views import blue, c

cache_config = {
    'CACHE_TYPE':'redis',
    # REDIS所在的主机
    'CACHE_REDIS_HOST':'localhost',
    'CACHE_REDIS_PORT':6379,    # Redis端口
    'CACHE_REDIS_DB':3,   # Redis数据库索引
}


def create_app():
    app = Flask(__name__)
    app.register_blueprint(blue)
    c.init_app(app,config=cache_config)  # Cache对象与程序实例关联，并且设置缓存配置信息
    return app