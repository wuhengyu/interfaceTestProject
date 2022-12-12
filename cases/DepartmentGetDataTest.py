# -*- coding: utf-8 -*-
# @Time    : 2022/12/13 0:43
# @Author  : Walter
# @File    : DepartmentGetDataTest.py
# @License : (C)Copyright Walter
# @Desc    :

import json

from base import HTTPClient
from base.GetInitData import GetInitData
from base.HTTPClient import HTTPClient
from cases.AccessTokenDataTest import AccessTokenDataTest
from utils.MysqlDB import db


class DepartmentCreateDataTest:
    def DepartmentGet(self):
        accessTokenDataTest = AccessTokenDataTest()
        param = eval(accessTokenDataTest.AccessToken())
        param = "access_token=" + param
        data = db.selectFetchone("interface_data", columns=["interfaceParams"], condition="interfaceName='department/get'")
        for x in data:
            data = json.loads(x)
        getInitData = GetInitData()
        url = getInitData.getDepartmentGetUrl()
        if isinstance(data, dict):
            http_client = HTTPClient()
            response_data = http_client.run("post", url, param, data)
            response_json = response_data.json()
            if response_json['errcode'] == 0:
                response_json = json.dumps(response_json)
                db.insertOneJson("response_data", "responseData", response_json)
                print("获取单条部门成功, ", response_json)
            else:
                response_json = json.dumps(response_json)
                db.insertOneJson("response_data", "responseData", response_json)
                print("获取单条部门失败, ", response_json)
            db.commit()
            db.close()
        else:
            print("data参数异常")

DepartmentCreateDataTest().DepartmentGet()