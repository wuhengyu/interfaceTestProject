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

    def readIniFilePath(self, file_name):
        file_path = self.base_path + '\\config\\' + file_name
        if not os.path.exists(file_path) or not os.path.isfile(file_path):
            raise ValueError("Invalid file path: {}".format(file_path))
        else:
            self.iniReader = IniReader(file_path)

    def GetWeixinHostPath(self):
        weixinHostPath = self.readIniFilePath('weiXinHostPath.ini')
        return weixinHostPath

    def getApiInterFace(self):
        apiInterFace = self.readIniFilePath('apiInterFace.ini')
        return apiInterFace

    def getBaseUrl(self):
        self.GetWeixinHostPath()
        base_url = self.iniReader.get_value('hostPath', 'host')
        return base_url

    def getAcessTokenUrl(self):
        self.getApiInterFace()
        acess_token_url = self.iniReader.get_value('getToken', 'get_token')
        return acess_token_url

    def getTokenUrl(self):
        access_token_url = self.getAcessTokenUrl()
        getTokenUrl = self.getBaseUrl() + access_token_url
        return getTokenUrl

    def getDepartmentCreateUrl(self):
        self.getApiInterFace()
        get_Department_Create_Url = self.iniReader.get_value('getDepartment', 'department_create')
        get_Department_Create_Url = self.getBaseUrl() + get_Department_Create_Url
        return get_Department_Create_Url


    def getDepartmentUpdateUrl(self):
        self.getApiInterFace()
        get_Department_Update_Url = self.iniReader.get_value('getDepartment', 'department_update')
        get_Department_Update_Url = self.getBaseUrl() + get_Department_Update_Url
        return get_Department_Update_Url

    def getDepartmentGetUrl(self):
        self.getApiInterFace()
        get_Department_Get_Url = self.iniReader.get_value('getDepartment', 'department_get')
        get_Department_Get_Url = self.getBaseUrl() + get_Department_Get_Url
        return get_Department_Get_Url

    def getDepartmentSimplelistUrl(self):
        self.getApiInterFace()
        get_Department_Simplelist_Url = self.iniReader.get_value('getDepartment', 'department_simplelist')
        get_Department_Simplelist_Url = self.getBaseUrl() + get_Department_Simplelist_Url
        return get_Department_Simplelist_Url
