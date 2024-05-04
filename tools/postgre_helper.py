# -*- coding: utf-8 -*-
"""
@Time ： 2023/6/19 11:52
@Auth ： sunwenjun
@File ：db_helper.py
@IDE ：PyCharm
@Brief：postgreSQL 数据库连接
"""
import numpy as np
import psycopg2 as pg
# pip install psycopg2


class DBHelper(object):
    def __init__(self, db_conf):
        self.host = db_conf["host"]
        self.user = db_conf['user']
        self.password = db_conf['password']
        self.database = db_conf['database']
        self.port = db_conf['port']

        # 建立数据库连接
        self.con = pg.connect(host=self.host, user=self.user,
                              password=self.password,
                              database=self.database, port=self.port)

        # 调用游标对象
        self.cursor = self.con.cursor()

    def select(self, sql):
        self.cursor.execute(sql)
        data_list = self.cursor.fetchall()
        data_list = np.char.array(data_list)
        return data_list

    def execute(self, sql):
        '''
        提交更改，增添或者修改数据必须提交才能生效
        :param sql:
        :return:
        '''
        self.cursor.execute(sql)
        self.con.commit()
        return

    def close(self):
        self.cursor.close()
        self.con.close()
