# -*- coding: utf-8 -*-
# @Time    : 2022/12/10 1:33
# @Author  : Walter
# @File    : MysqlDB.py
# @License : (C)Copyright Walter
# @Desc    :
import json

import pymysql

class MySQLDB:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

        self.connection = pymysql.connect(
            host=self.host,
            user=self.user,
            password=self.password,
            database=self.database
        )

        self.cursor = self.connection.cursor()

    def execute(self, sql):
        self.cursor.execute(sql)

    def commit(self):
        self.connection.commit()

    def fetchone(self):
        return self.cursor.fetchone()

    def fetchall(self):
        return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def insert(self, table, data):
        """
        向数据库中插入一条数据
        :param table: 表名
        :param data: 插入的数据，字典形式，例如：{"name": "zhangsan", "age": 18}
        """
        columns = ', '.join(data.keys())
        values = ', '.join(["%s"] * len(data))
        sql = f"INSERT INTO {table}({columns}) VALUES ({values})"
        self.cursor.execute(sql, tuple(data.values()))

        # 检查插入操作是否执行成功
        if self.cursor.rowcount > 0:
            print("插入成功")
        else:
            print("插入失败")


    def insertOneJson(self, table, columns, data):
        """
        向数据库中插入一条数据
        :param table: 表名
        :param data: 插入的数据，字典形式，例如：{"name": "zhangsan", "age": 18}
        """
        sql = f"INSERT INTO {table}({columns}) VALUES (%s)"
        self.cursor.execute(sql, (data,))

        # 检查插入操作是否执行成功
        if self.cursor.rowcount > 0:
            print("插入成功")
        else:
            print("插入失败")


    def update(self, table, data, condition):
        """
        更新数据库中的一条数据
        :param table: 表名
        :param data: 更新的数据，字典形式，例如：{"name": "zhangsan", "age": 18}
        :param condition: 更新条件，字符串形式，例如："id=1"
        """
        set_data = ', '.join([f"{key}=%s" for key in data.keys()])
        sql = f"UPDATE {table} SET {set_data} WHERE {condition}"
        self.cursor.execute(sql, tuple(data.values()))

    def delete(self, table, condition):
        """
        删除数据库中的一条数据
        :param table: 表名
        :param condition: 删除条件，字符串形式，例如："id=1"
        """
        sql = f"DELETE FROM {table} WHERE {condition}"
        self.cursor.execute(sql)

    def count(self, table, condition=None):
        """
        统计表中满足条件的记录数量
        :param table: 表名
        :param condition: 查询条件，字符串形式，例如："age > 18"
        :return: 记录数量
        """
        if condition:
            sql = f"SELECT COUNT(*) FROM {table} WHERE {condition}"
        else:
            sql = f"SELECT COUNT(*) FROM {table}"
        self.cursor.execute(sql)
        count = self.cursor.fetchone()[0]
        return count

    def exists(self, table, condition):
        """
        判断表中是否存在满足条件的记录
        :param table: 表名
        :param condition: 查询条件，字符串形式，例如："age > 18"
        :return: 如果存在，返回 True；否则返回 False
        """
        count = self.count(table, condition)
        return count > 0

    def selectFetchall(self, table, columns=None, condition=None):
        """
        从数据库中查询数据
        :param table: 表名
        :param columns: 查询的列名，字符串列表形式，例如：["name", "age"]
        :param condition: 查询条件，字符串形式，例如："age > 18"
        :return: 查询结果
        """
        if columns:
            columns = ', '.join(columns)
        else:
            columns = '*'
        if condition:
            sql = f"SELECT {columns} FROM {table} WHERE {condition}"
        else:
            sql = f"SELECT {columns} FROM {table}"

        self.cursor.execute(sql)
        results = self.cursor.fetchall()
        return results

    def selectFetchone(self, table, columns=None, condition=None):
        """
        从数据库中查询数据
        :param table: 表名
        :param columns: 查询的列名，字符串列表形式，例如：["name", "age"]
        :param condition: 查询条件，字符串形式，例如："age > 18"
        :return: 查询结果
        """
        if columns:
            columns = ', '.join(columns)
        else:
            columns = '*'
        if condition:
            sql = f"SELECT {columns} FROM {table} WHERE {condition}"
        else:
            sql = f"SELECT {columns} FROM {table}"

        self.cursor.execute(sql)
        results = self.cursor.fetchone()
        return results


db = MySQLDB(host="192.168.81.188", user="root", password="123456", database="interfaceTestProject")

# data = {'errcode': 0, 'errmsg': 'ok', 'access_token': 'R2pYKjYEUgLbMkUDRkjtenBUKwDOPiw8jvUQbg1a5fxcp80rmuOOpEQzw6PdLsCize6CI7oRxuQt9AWDUjG882PyHC259EyQs5GrXVHPBdPf_NWuopmDdPON9-oZW83yg3Basrg-DANqbf1CPlmThZ2TKHP4kXdiFanGXCtx4gLlgqOEovA2Ea_8X_B2risdcVVhp812gvhq2Qe5po1jTQ', 'expires_in': 7200}
# data = json.dumps(data)
# db.insertOneJson("response_data", "responseData", data)
#
# db.commit()
# db.close()

# 更新数据
# db.update("table", {"name": "lisi"}, "id=1")

# 删除数据
# db.delete("table", "id=1")

# 统计记录数量
# count = db.count("table")

# 判断是否存在满足条件的记录
# exists = db.exists("table", "age > 18")

# 查询数据
# results = db.select("table", columns=["name", "age"], condition="age > 18")
# results = db.select("interface_data", columns=["id", "interfaceName"])
# print(results)

# # 使用 format() 方法来构建查询
# query = "INSERT INTO users (username, email) VALUES ({}, {})".format("%s", "%s")
# args = ("johndoe", "johndoe@example.com")
# cursor.execute(query, args)
#
# # 使用 executemany() 方法来执行批量插入
# query = "INSERT INTO users (username, email) VALUES (%s, %s)"
# args = [("johndoe", "johndoe@example.com"), ("janedoe", "janedoe@example.com")]
# cursor.executemany(query, args)


