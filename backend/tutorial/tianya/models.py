import sqlite3
import os


class Sqlite(object):
    def __init__(self):
        # sqlite3.connect数据库连接
        self.conn = sqlite3.connect("TianYaLunTan.db", check_same_thread=False)
        # self.conn.cursor()创建游标
        self.curs = self.conn.cursor()

    def close_db(self):
        # self.curs.close()关闭游标
        self.curs.close()
        # self.conn.close()关闭数据库
        self.conn.close()

    def select_sql(self, sql_, *data):
        try:
            # self.curs.execute(sql_, *data)执行sql语句
            self.curs.execute(sql_, *data)
            # self.curs.fetchone()查询一条数据
            # self.curs.fetchall()查询所有所有
            result = self.curs.fetchall()
            print("select_sql", 1, sql_)
            if result:
                return list(result)
            return None
        except Exception as error:
            print("select_sql", 0, error)

    def upDate_sql(self, sql_, *data):
        try:
            self.curs.execute(sql_, *data)
            self.conn.commit()
            print("upData_sql", 1, sql_)
        except Exception as error:
            print("upData_sql", 0, error)
            self.conn.rollback()

    def insert_sql(self, sql_, *data):
        try:
            self.curs.execute(sql_, *data)
            self.conn.commit()
            print("insert_sql", 1, sql_)
        except Exception as error:
            print("insert_sql", 0, error)
            self.conn.rollback()

    def del_sql(self, sql_, *data):
        try:
            self.curs.execute(sql_, *data)
            self.conn.commit()
            print("del_sql", 1, sql_)
        except Exception as error:
            print("del_sql", 0, error)
            self.conn.rollback()

    def create_table(self, sql_):
        try:
            self.curs.execute(sql_)
            self.conn.commit()
            print("create_table:", 1, sql_)
        except Exception as error:
            print("create_table:", 0, error)
            self.conn.rollback()


if __name__ == '__main__':
    run_sql = Sqlite()

    # # 创建表
    # sql = """
    # CREATE TABLE login_bi(
    # id INTEGER PRIMARY KEY AUTOINCREMENT,
    # cookie TEXT,
    # username TEXT,
    # passWord TEXT)
    # """
    # print(run_sql.create_table(sql))


    # 插入数据
    # cookie = "2"
    # userName = 'admin'
    # passWord = 'admin'
    #
    # sql = """
    # insert into login_bi('cookie','username','password') values (?,?,?)
    # """
    # datas = (cookie, userName, passWord)
    # run_sql.insert_sql(sql, datas)

    # 删除数据
    # print(run_sql.del_sql("delete from login where username='admin'"))

    # 查询数据
    print(run_sql.select_sql("select * from TianYanLunTan"))
