from ManytoManyApp.ext import db

# Table对象对应第三方中间表，指定表名称和两个外键列
ug_relation = db.Table("user_group",
         db.Column("user_id",db.Integer,db.ForeignKey("users.id"),primary_key=True),
         db.Column("group_id",db.Integer,db.ForeignKey("groups.id"),primary_key=True)
         )


class User(db.Model):    # 用户多方表
    __tablename__ = "users"
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(20),nullable=False)
    ugroups = db.relationship("Group",secondary=ug_relation,backref="gusers")   #  主动关联Group模型和第三方表，并给Group添加反向引用


class Group(db.Model):   # 组多方表
    __tablename__ = "groups"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    groupname = db.Column(db.String(20),nullable=False)