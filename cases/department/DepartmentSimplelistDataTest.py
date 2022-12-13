# -*- coding: utf-8 -*-
# @Time    : 2022/12/13 0:57
# @Author  : Walter
# @File    : DepartmentSimplelistDataTest.py
# @License : (C)Copyright Walter
# @Desc    :

import json

from base import HTTPClient
from base.GetInitData import GetInitData
from base.HTTPClient import HTTPClient
from cases.AccessTokenDataTest import AccessTokenDataTest
from utils.MysqlDB import db


class DepartmentSimplelistDataTest:
    def DepartmentSimplelist(self):
        accessTokenDataTest = AccessTokenDataTest()
        param = eval(accessTokenDataTest.AccessToken())
        param = "access_token=" + param
        data = db.selectFetchone("interface_data", columns=["interfaceParams"], condition="interfaceName='department/simplelist'")
        for x in data:
            data = json.loads(x)
        getInitData = GetInitData()
        url = getInitData.getDepartmentSimplelistUrl()
        if isinstance(data, dict):
            http_client = HTTPClient()
            response_data = http_client.run("post", url, param, data)
            response_json = response_data.json()
            if response_json['errcode'] == 0:
                response_json = json.dumps(response_json)
                db.insertOneJson("response_data", "responseData", response_json)
                print("获取部门ID成功, ", response_json)
            else:
                response_json = json.dumps(response_json, ensure_ascii=False, indent=4, sort_keys=True)
                db.insertOneJson("response_data", "responseData", response_json)
                print("获取部门ID失败, ", response_json)
            try:
                db.commit()
            except Exception as e:
                print("An error occurred:", e)

            db.close()
        else:
            print("data参数异常")

DepartmentSimplelistDataTest().DepartmentSimplelist()