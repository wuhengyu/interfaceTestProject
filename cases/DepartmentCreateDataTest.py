# -*- coding: utf-8 -*-
# @Time    : 2022/12/12 14:00
# @Author  : Walter
# @File    : DepartmentCreateDataTest.py
# @License : (C)Copyright Walter
# @Desc    :
import json

from base import HTTPClient
from base.HTTPClient import HTTPClient
from utils import ReaderNewToken
from utils.MysqlDB import db

class DepartmentCreateDataTest:
    def DepartmentCreate(self):
        newToken = ReaderNewToken.ReaderNewToken()
        param = newToken
        data = db.selectFetchone("interface_data", columns=["interfaceParams"], condition="interfaceName=department/create")
        data = json.loads(data)

        url = db.selectFetchone("interface_data", columns=["interfaceName"], condition="interfaceName=department/create")
        http_client = HTTPClient()
        http_client.run("post", url, param, data)
        # accessToken = db.selectFetchone("access_token_data", "accessTokenData")