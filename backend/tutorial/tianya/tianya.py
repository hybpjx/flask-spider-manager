from flask_cors import *
from flask import Blueprint, jsonify
from flask_login import LoginManager
import sqlite3

ty = Blueprint('ty', __name__)

login_manager = LoginManager()
login_manager.login_view = 'ty'  ###跳转登录的地址
login_manager.session_protection = 'strong'


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


run_sql = Sqlite()


@ty.route('/ty', methods=('GET', 'POST'))
@cross_origin()
def get_data():
    data_list = run_sql.select_sql("select * from TianYanLunTan")
    item_list = []
    for data in data_list:
        item = {}
        item['title'] = data[0]
        item['title_url'] = data[1]
        item['author'] = data[2]
        item['click_number'] = data[3]
        item['replies_number'] = data[4]
        item['publish_date'] = data[5]
        item['description'] = data[6]
        item_list.append(item)
    return jsonify(item_list)
