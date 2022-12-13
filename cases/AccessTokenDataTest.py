# -*- coding: utf-8 -*-
# @Time    : 2022/12/10 23:03
# @Author  : Walter
# @File    : AccessTokenDataTest.py
# @License : (C)Copyright Walter
# @Desc    :
import json

from base.GetInitData import GetInitData
from base.HTTPClient import headers, HTTPClient
from utils.MysqlDB import db


class AccessTokenDataTest:
    def AccessToken(self):
        http_client = HTTPClient()
        params = db.selectFetchone("interface_data", columns=["interfaceParams"])
        response_json = None
        response_accessTokenData = None
        for param in params:
            params_json = json.loads(param)
            if param is not None:
                getInitData = GetInitData()
                getTokenUrl = getInitData.getTokenUrl()
                response_data = http_client.run('get', getTokenUrl, params_json, headers)
                response_json = response_data.json()
                if response_json['errcode'] == 0:
                    response_accessTokenData = response_json['access_token']
                    response_accessTokenData = json.dumps(response_accessTokenData)
                    db.insertOneJson("access_token_data", "accessTokenData", response_accessTokenData)
                    print("获取access_token成功:\n", response_accessTokenData)
                else:
                    print("获取access_token失败:\n", response_accessTokenData)
                    response_accessTokenData = json.dumps(response_accessTokenData)
                    db.insertOneJson("access_token_data", "accessTokenData", response_accessTokenData)
                db.commit()
            else:
                print("params_dict参数异常")
        return response_accessTokenData

# accessTokenData = AccessTokenDataTest()
# accessTokenData.AccessToken()
# db.close()