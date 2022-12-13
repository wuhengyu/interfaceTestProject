# -*- coding: utf-8 -*-
# @Time    : 2022/12/12 14:00
# @Author  : Walter
# @File    : CalendarAddDataTest.py
# @License : (C)Copyright Walter
# @Desc    :
import json

from base import HTTPClient
from base.GetInitData import GetInitData
from base.HTTPClient import HTTPClient
from cases.AccessTokenDataTest import AccessTokenDataTest
from utils.MysqlDB import db


class CalendarAddDataTest:
    def CalendarAdd(self):
        accessTokenDataTest = AccessTokenDataTest()
        param = eval(accessTokenDataTest.AccessToken())
        param = "access_token=" + param
        data = db.selectFetchone("interface_data", columns=["interfaceParams"], condition="interfaceName='oa/calendar/add'")
        for x in data:
            data = json.loads(x)
        getInitData = GetInitData()
        url = getInitData.getCalendarAddUrl()
        if isinstance(data, dict):
            http_client = HTTPClient()
            response_data = http_client.run("post", url, param, data)
            response_json = response_data.json()
            if response_json['errcode'] == 0:
                response_json = json.dumps(response_json)
                db.insertOneJson("response_data", "responseData", response_json)
                print("创建日历成功:", response_json)
            else:
                print("创建日历失败:", json.dumps(response_json, ensure_ascii=False, indent=4, sort_keys=True))
                response_json = json.dumps(response_json)
                db.insertOneJson("response_data", "responseData", response_json)
            db.commit()
            db.close()
        else:
            print("data参数异常")

CalendarAddDataTest().CalendarAdd()