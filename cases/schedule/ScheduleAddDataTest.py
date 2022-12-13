# -*- coding: utf-8 -*-
# @Time    : 2022/12/12 22:34
# @Author  : Walter
# @File    : ScheduleAddDataTest.py
# @License : (C)Copyright Walter
# @Desc    :
import json

from base.GetInitData import GetInitData
from base.HTTPClient import HTTPClient
from cases.AccessTokenDataTest import AccessTokenDataTest
from utils.MysqlDB import db


class ScheduleAddDataTest:
    def ScheduleAdd(self):
        accessTokenDataTest = AccessTokenDataTest()
        param = eval(accessTokenDataTest.AccessToken())
        param = "access_token=" + param
        data = db.selectFetchone("interface_data", columns=["interfaceParams"], condition="interfaceName='oa/schedule/add'")
        for x in data:
            data = json.loads(x)
        getInitData = GetInitData()
        url = getInitData.getScheduleAddUrl()
        if isinstance(data, dict):
            http_client = HTTPClient()
            response_data = http_client.run("post", url, param, data)
            response_json = response_data.json()
            if response_json['errcode'] == 0:
                response_json = json.dumps(response_json)
                db.insertOneJson("response_data", "responseData", response_json)
                print("创建日程成功, ", response_json)
            else:
                response_json = json.dumps(response_json)
                db.insertOneJson("response_data", "responseData", response_json)
                print("创建日程失败, ", response_json)
            db.commit()
            db.close()
        else:
            print("data参数异常")

ScheduleAddDataTest().ScheduleAdd()