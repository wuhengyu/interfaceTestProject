# -*- coding: utf-8 -*-
# @Time    : 2022/12/10 23:03
# @Author  : Walter
# @File    : AccessToken.py
# @License : (C)Copyright Walter
# @Desc    :
import json

from base.GetInitData import getTokenUrl
from base.HttpClient import headers, HttpClient
from utils.MysqlDB import db


class AccessTokenData():
    def AccessToken(self):
        http_client = HttpClient()
        params = db.selectFetchone("interface_data", columns=["interfaceParams"])
        response_json = None
        response_accessTokenData = None
        for param in params:
            params_json = json.loads(param)
            if param is not None:
                response_data = http_client.run('get', getTokenUrl, params_json, headers)
                response_json = response_data.json()
                if response_json['errcode'] == 0:
                    response_accessTokenData = response_json['access_token']
                else:
                    db.insertOneJson("response_data", "responseData", response_json)
                    print("获取access_token失败", response_json)
            else:
                print("params_dict参数异常")

        response_json = json.dumps(response_json)
        db.insertOneJson("response_data", "responseData", response_json)
        db.insertOneJson("access_token_data", "accessTokenData", response_accessTokenData)
        db.commit()
        db.close()


accessTokenData = AccessTokenData()
accessTokenData.AccessToken()
