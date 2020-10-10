import sys
#sys.path.append("F:\\Python1905_Project\FlaskDay3")  # 将该绝对路径加入搜索路径
sys.path.append(".")  # 将当前命令行中的目录加入搜索路径

from flask_script import Manager

from BlueprintApp import create_app

app = create_app()
manager = Manager(app)


if __name__ == '__main__':
    manager.run()


