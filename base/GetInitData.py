# -*- coding: utf-8 -*-
# @Time    : 2022/12/9 23:28
# @Author  : Walter
# @File    : GetInitData.py
# @License : (C)Copyright Walter
# @Desc    :
import os
from utils.IniReader import IniReader


class GetInitData:
    def __init__(self):
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        self.init_data = GetInitData()

    def readIniFile(self, file_name):
        file_path = self.base_path + '/config/' + file_name
        if not os.path.exists(file_path) or not os.path.isfile(file_path):
            raise ValueError("Invalid file path: {}".format(file_path))
        else:
            self.reader = IniReader(file_path)

    def getBaseUrl(self):
        base_url = self.reader.get_value('hostPath', 'host')
        return base_url

    def getAcessTokenUrl(self):
        acess_token_url = self.reader.get_value('getToken', 'get_token')
        return acess_token_url

    def getTokenUrl(self):
        self.init_data.readIniFile('weixinHostPath.ini')
        base_url = self.init_data.getBaseUrl()

        self.init_data.readIniFile('apiInterFace.ini')
        access_token_url = self.init_data.getAcessTokenUrl()
        getTokenUrl = base_url + access_token_url
        return getTokenUrl

    def getDepartmentCreate(self):
        get_Department_CreateUrl = self.reader.get_value('getDepartment', 'department_create')
        get_Department_CreateUrl = self.getBaseUrl() + get_Department_CreateUrl
        return get_Department_CreateUrl
