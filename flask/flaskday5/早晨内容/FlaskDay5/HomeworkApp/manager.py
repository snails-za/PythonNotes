import sys
sys.path.append(".")

from flask_migrate import Migrate, MigrateCommand
from HomeworkApp import create_app
from HomeworkApp.models import db
from flask_script import Manager


app = create_app()
manager = Manager(app)
Migrate(app,db)
manager.add_command("nicedb",MigrateCommand)

if __name__ == '__main__':
    manager.run()