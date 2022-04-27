# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import re
import sqlite3

from itemadapter import ItemAdapter
# import pymysql


class SpiderproPipeline:
    fp=None


    def open_spider(self,spider):
        print('开始爬虫')
        self.fp=open('tianya.txt','w+',encoding='utf-8')

    def process_item(self, item, spider):

        self.fp.write(str(item))

        return item

    def close_spider(self,spider):
        self.fp.close()
        print('结束爬虫')


# class MysqlPipeLine:
#     conn = None
#     cursor = None
#
#     def open_spider(self, spider):
#         self.conn = pymysql.Connect(host='192.168.244.142',
#                                     port=3306,
#                                     database='spider',
#                                     charset='utf8',
#                                     user='root',
#                                     password='admin*123', )
#
#     def process_item(self, item, spider):
#         self.cursor = self.conn.cursor()
#
#
#
#         try:
#             title = item['title']
#             author = item['author']
#             click = item['click']
#
#             title = title.strip()
#             title = re.sub(' ', '', title)
#             self.cursor.execute('insert into tianya_plate (title,author,click) values ("%s","%s","%s")'
#                                 % (title, author, click))
#             self.conn.commit()
#         except Exception as e:
#
#             print(e)
#             self.conn.rollback()
#
#         return item
#
#     def close_spider(self, spider):
#         self.cursor.close()
#         self.conn.close()


class Sqlite3Pipeline:
    def __init__(self, sqlite_file):
        self.sqlite_file = sqlite_file

    @classmethod
    def from_crawler(cls, crawler):
        """
        @classmethod
            - 无需实例化
            - 可以调用类属性和类方法
            - 无法取到普通的成员属性和方法
        :param crawler:
        :return:
        """
        return cls(
            sqlite_file=crawler.settings.get('SQLITE_FILE'),
        )  # 从 settings.py 提取

    def open_spider(self, spider):
        self.conn = sqlite3.connect(self.sqlite_file)  # 连接数据库
        self.cur = self.conn.cursor()  # 添加游标

    def process_item(self, item, spider):
        sql = "CREATE TABLE TianYanLunTan( " \
              "title VARCHAR(255), " \
              "title_url varchar(255)," \
              "author varchar(255)," \
              "click_number varchar(255)," \
              "replies_number varchar(255)," \
              "publish_date varchar(255)," \
              "description varchar(255))"  # 此处为原生SQL语句字段为
        try:
            self.cur.execute(sql)  # 创建country的表
        except:
            pass
        sql_insert = """insert into TianYanLunTan 
        values (?,?,?,?,?,?,?)"""
        param = (item['title'],
                 item['title_url'],
                 item['author'],
                 item['click_number'],
                 item['replies_number'],
                 item['publish_date'],
                 item['description'],
                 )
        self.cur.execute(sql_insert, param)
        self.conn.commit()  # 保存

        return item

    def close_spider(self, spider):
        self.conn.close()

