# -*- coding: utf-8 -*-
# @Time    : 2022/12/12 14:00
# @Author  : Walter
# @File    : DepartmentCreate.py
# @License : (C)Copyright Walter
# @Desc    :
from base import HttpClient
from utils import ReaderNewToken, MysqlDB


def DepartmentCreate():
    NewToken = ReaderNewToken.ReaderNewToken()
    data = MysqlDB.MySQLDB.selectFetchone("access_token_data", )
    HttpClient.HttpClient.run("post", data, )
