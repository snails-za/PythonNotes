import sys
sys.path.append(".")

from flask_migrate import Migrate, MigrateCommand
from ManytoManyApp import create_app
from ManytoManyApp.models import db
from flask_script import Manager


app = create_app()
manager = Manager(app)
Migrate(app,db)
manager.add_command("nicedb",MigrateCommand)  # 自定义数据库迁移命令

if __name__ == '__main__':
    manager.run()