# -*- coding: utf-8 -*-
# @Time    : 2022/12/10 23:03
# @Author  : Walter
# @File    : AccessToken.py
# @License : (C)Copyright Walter
# @Desc    :
import json

from base.GetInitData import getTokenUrl
from base.HttpClient import http_client, headers
from utils.MysqlDB import db

def AccessToken():
    params = db.selectFetchone("interface_data", columns=["interfaceParams"])

    # for param in params:
    #     for params_json in param:
    #         params_json = json.loads(params_json)
    #         http_client.run('get', getTokenUrl, params_json)

    response_json = {}
    response_accessTokenData = []
    for param in params:
        for i, params_dict in enumerate(param):
            if params_dict is not None:
                # params_dict = json.loads(json.dumps(params_dict))
                params_dict = json.loads(params_dict)
                response_data = http_client.run('get', getTokenUrl, params_dict, headers)
                response_json = response_data.json()
                if response_json['errcode'] == 0:
                    response_accessTokenData = response_json['access_token']
                else:
                    print("未找到access_token，", response_json)

    response_json = json.dumps(response_json)
    db.insertOneJson("response_data", "responseData", response_json)
    db.insertOneJson("access_token_data", "accessTokenData", response_accessTokenData)
    db.commit()
    db.close()
