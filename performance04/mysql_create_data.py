# -*- coding: UTF-8 -*-

"""在数据库中创建500w行数据"""
import json
import queue
from threading import Thread

from mysql.connector import connect


class DBOperate(Thread):
    """并发操作数据库，并发创建数据"""
    __count = 0

    def __init__(self):
        super().__init__()
        with open("./data.json", "r") as file:
            conf = json.load(file)
        self.host = conf.get("host", "127.0.0.1")
        self.user = conf.get("user", "test")
        self.pwd = conf.get("password", "123456")
        self.database = conf.get("database", "test")
        self.db = connect(host=self.host, user=self.user, password=self.pwd, database=self.database)
        self.cursor = self.db.cursor()

        if DBOperate.__count == 0:  # 表只创建一次
            self.create_table()
            DBOperate.__count += 1

    def create_table(self):
        """创建表"""
        self.cursor.execute("drop table if exists llt_test")  # 防止创建错误，先删除
        sql = """
create table llt_test(
id int auto_increment primary key,
name varchar(50) not null,
card_id varchar(50) not null unique)
"""
        self.cursor.execute(sql)

    def insert_data(self, value):
        """插入数据"""
        sql = "insert into llt_test (name, card_id) values(%s, %s)"
        self.cursor.execute(sql, value)
        self.db.commit()

    def run(self):
        while True:
            if q.empty():
                break
            value = q.get(True)
            print(f"{self.name} ==> {value}")
            self.insert_data(value)
        self.un_connect()

    def un_connect(self):
        self.cursor.close()
        self.db.close()


def create_data() -> queue.Queue:
    qu = queue.Queue()
    for i in range(1, 100001):
        name = f"name_{i}"
        card_id = f"{i:0>18}"
        qu.put((name, card_id))
    return qu


if __name__ == '__main__':
    q = create_data()

    ts = [DBOperate() for _ in range(50)]  # 50个线程创建10w条数据
    for t in ts:
        t.start()
    for t in ts:
        t.join()
    print("数据创建完成")
