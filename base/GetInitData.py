# -*- coding: utf-8 -*-
# @Time    : 2022/12/9 23:28
# @Author  : Walter
# @File    : getIniFile.py
# @License : (C)Copyright Walter
# @Desc    :
import os

from utils.IniReader import IniReader


class GetInitData():
    def __init__(self):
        self.base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

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


init_data1 = GetInitData()
init_data1.readIniFile('getToken.ini')
base_url = init_data1.getBaseUrl()

init_data2 = GetInitData()
init_data2.readIniFile('apiInterFace.ini')
access_token_url = init_data2.getAcessTokenUrl()

getTokenUrl = base_url + access_token_url
# print(getTokenUrl)
