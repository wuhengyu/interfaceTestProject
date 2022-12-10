# -*- coding: utf-8 -*-
# @Time    : 2022/12/9 17:35
# @Author  : Walter
# @File    : HttpClient.py
# @License : (C)Copyright Walter
# @Desc    :
import json

import requests

from base.GetInitData import getTokenUrl
from utils.MysqlDB import db


class HttpClient:
    def __init__(self, cookies=None, headers=None, response_accessToken=None):
        self.session = requests.Session()
        self.cookies = cookies
        self.headers = headers

    def get(self, url, params=None):
        response = self.session.get(url, params=params, cookies=self.cookies, headers=self.headers)
        return response

    def post(self, url, params=None, data=None, json=None):
        response = self.session.post(url, params=params, data=data, json=json, cookies=self.cookies, headers=self.headers)
        return response

    def put(self, url, data):
        response = self.session.put(url, data=data, headers=self.headers)
        return response

    def delete(self, url):
        response = self.session.delete(url, headers=self.headers)
        return response

    def run(self, method, url, params=None, data=None):
        if method == "get":
            response = self.get(url, params=params)
        elif method == "post":
            response = self.post(url, params=params, data=data)
        elif method == "put":
            response = self.put(url, data=data)
        elif method == "delete":
            response = self.delete(url)
        else:
            raise ValueError("Invalid method")
        return response


headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"
}
http_client = HttpClient()
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
