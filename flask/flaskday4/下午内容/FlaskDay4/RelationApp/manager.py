import sys
sys.path.append(".")

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from RelationApp import create_app
from RelationApp.models import db

app = create_app()
Migrate(app,db)   # 目的是创建migrations目录
manager = Manager(app)
manager.add_command("nicedb",MigrateCommand)  # 自定义迁移命令


if __name__ == '__main__':
    manager.run()