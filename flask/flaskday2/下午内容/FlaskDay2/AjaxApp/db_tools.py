import pymysql


def get_conn():   # 获取数据库连接对象
    conn = pymysql.connect(
        host="localhost",
        port=3306,
        user="root",
        password="123456",
        database="mydb",
        charset="utf8"
    )
    return conn


def regname_is_exists(regname):    # 根据注册用户名查询数据库，返回该注册名是否在库中存在
    conn = get_conn()
    cursor = conn.cursor()
    sql = "select * from users where username='{}'".format(regname)
    try:
        cursor.execute(sql)
        item = cursor.fetchone()
        conn.commit()
        if item:    #  如果客户端传递的注册用户名在数据库中已存在
            return True
        else:
            return False
    except Exception as e:
        conn.rollback()
        print("操作数据库异常，异常原因：",e)
    finally:
        cursor.close()
        conn.close()