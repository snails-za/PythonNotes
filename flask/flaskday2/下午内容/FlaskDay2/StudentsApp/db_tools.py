import pymysql

from StudentsApp.po import Student


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


def select_allstudents():   # 查询所有的学生
    students = []   # 存储学生对象的列表
    conn = get_conn()
    cursor = conn.cursor()
    sql = "select id,name,sex,score from students"
    try:
        cursor.execute(sql)
        items = cursor.fetchall()
        conn.commit()
        for item in items:
            stu = Student(item[0],item[1],item[2],item[3])  # 将数据库表的数据查出，封装到Student对象中
            students.append(stu)
        return students
    except Exception as e:
        conn.rollback()
        print("查询学生错误，错误原因：",e)
    finally:
        cursor.close()
        conn.close()


def select_detail_student(stuid):   # 根据学生ID查询学生信息
    conn = get_conn()
    cursor = conn.cursor()
    sql = f"select id,name,sex,score from students where id={stuid}"
    try:
        cursor.execute(sql)
        item = cursor.fetchone()
        conn.commit()
        student = Student(item[0],item[1],item[2],item[3])  # 将学生信息封装到Student对象中
        return student
    except Exception as e:
        conn.rollback()
        print("查询学生错误，错误原因：", e)
    finally:
        cursor.close()
        conn.close()
