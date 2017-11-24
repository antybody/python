# -*- coding: utf8 -*-
from datetime import date

import mysql.connector


class myconnect:
    def __init__(self,config):
        self.config = config
        #self.cursor = self.get_conn()
    # 获取连接
    def get_conn(self):
        try:
            # 设定数据库连接信息
            conn = mysql.connector.connect(**self.config)
            # 开启数据库操作的cursor
            # cursor = conn.cursor()
            # 指定操作SQL
            # sql_query = 'select code from tb_code;'
            # 执行操作SQL
            # cursor.execute(sql_query)
            # 获取操作的结果集
            # results = cursor.fetchall()
            # 循环结果集
            # 提交
            # conn.commit()
            # 关闭cursor
            # cursor.close()
            # 关闭连接
            return conn
        except mysql.connector.Error as e:
            print('connect fails!{}'.format(e))
            conn.close()


    # 执行查询
    def get_select(self,cursor,sqltext,sqlparam=None):
        try:
            if sqlparam:
                cursor.execute(sqltext,sqlparam)
            else:
                cursor.execute(sqltext)
            results =cursor.fetchall()
            return results
        except mysql.connector.Error as err:
            print err

    # 执行insert
    def get_insert(self,cursor,sqltext,sqlparam):
        try:
            if sqlparam:
                cursor.execute(sqltext,sqlparam)
                print 'ok'
                # cursor.commit()
        except mysql.connector.Error as err:
            print err

    # 执行delete
    def get_del(self):
        pass

    # 执行update
    def get_update(self):
        pass

if __name__ == '__main__':
    config = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': 'mysql',
        'port': 3308,
        'database': 'test',
        'charset': 'utf8'
    }
    mysqlConnect = myconnect(config)
    mysqlConn = mysqlConnect.get_conn()
    mysqlCursor = mysqlConn.cursor()
    results = mysqlConnect.get_select(mysqlCursor,"select code from tb_code")
    for re in results:
        print re[0]

    insert_data = ('a','b',date(1977, 6, 14))
    mysqlConnect.get_insert(mysqlCursor,"insert into tb_code (code,name,time) VALUES (%s,%s,%s)",insert_data)
    try:
        mysqlConn.commit()
    except Exception as e:
        print(e)
        mysqlConn.rollback()