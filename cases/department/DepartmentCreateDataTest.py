# -*- coding: utf-8 -*-
# @Time    : 2022/12/12 14:00
# @Author  : Walter
# @File    : DepartmentCreateDataTest.py
# @License : (C)Copyright Walter
# @Desc    :
import json

from base import HTTPClient
from base.GetInitData import GetInitData
from base.HTTPClient import HTTPClient
from cases.AccessTokenDataTest import AccessTokenDataTest
from utils.MysqlDB import db


class DepartmentCreateDataTest:
    def DepartmentCreate(self):
        accessTokenDataTest = AccessTokenDataTest()
        param = eval(accessTokenDataTest.AccessToken())
        param = "access_token=" + param
        data = db.selectFetchone("interface_data", columns=["interfaceParams"], condition="interfaceName='department/create'")
        for x in data:
            data = json.loads(x)
        getInitData = GetInitData()
        url = getInitData.getDepartmentCreateUrl()
        if isinstance(data, dict):
            http_client = HTTPClient()
            response_data = http_client.run("post", url, param, data)
            response_json = response_data.json()
            if response_json['errcode'] == 0:
                response_json = json.dumps(response_json)
                db.insertOneJson("response_data", "responseData", response_json)
                print("创建部门成功:", response_json)
            else:
                print("创建部门失败:", json.dumps(response_json, ensure_ascii=False, indent=4, sort_keys=True))
                response_json = json.dumps(response_json)
                db.insertOneJson("response_data", "responseData", response_json)
            db.commit()
            db.close()
        else:
            print("data参数异常")

DepartmentCreateDataTest().DepartmentCreate()