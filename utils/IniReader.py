# -*- coding: utf-8 -*-
# @Time    : 2022/12/9 15:03
# @Author  : Walter
# @File    : handle_ini.py
# @License : (C)Copyright Walter
# @Desc    :
import configparser

class IniReader:
    def __init__(self, filename):
        self.filename = filename
        self.config = configparser.ConfigParser()
        self.config.read(self.filename, encoding="utf-8")

    def get_value(self, section, key):
        try:
            return self.config.get(section, key)
        except Exception:
            return "没有获取到文件key值"
