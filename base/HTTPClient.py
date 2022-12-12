# -*- coding: utf-8 -*-
# @Time    : 2022/12/9 17:35
# @Author  : Walter
# @File    : HTTPClient.py
# @License : (C)Copyright Walter
# @Desc    :
import requests


class HTTPClient:
    def __init__(self, cookies=None, headers=None):
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
