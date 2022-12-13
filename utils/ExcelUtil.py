# -*- coding: utf-8 -*-
# @Time    : 2022/12/13 15:18
# @Author  : Walter
# @File    : ExcelUtil.py
# @License : (C)Copyright Walter
# @Desc    :
'''
读取Excel文件：可以使用openpyxl库中的load_workbook()函数来读取Excel文件。
获取工作簿：可以使用openpyxl库中的get_sheet_by_name()函数来获取工作簿。
获取工作表：可以使用openpyxl库中的worksheets属性来获取工作表。
读取单元格内容：可以使用openpyxl库中的cell()函数来读取单元格内容。
写入单元格内容：可以使用openpyxl库中的cell()函数来写入单元格内容。
保存Excel文件：可以使用openpyxl库中的save()函数来保存Excel文件。
'''
import os

import xlrd

class OpeExcel:
    def __init__(self,file_name=None,sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = 'file_path/xxx.xls'
            self.sheet_id = 0
        self.data = self.get_data()

#获取sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    #获取单元格行数
    def get_lines(self):
        tables = self.data
        return tables.nrows

    #获取单元格数据
    def get_value(self,row,col):
        return self.data.cell_value(row,col)

    # 判断exce文件是否存在，不存在则创建，存在则直接打开编辑
    def excel_create(self):
        if not os.path.exists(self.filename):
            data = xlwt.Workbook()
            table = data.add_sheet(self.sheetname)
            table.write(0, 0, "id")
            data.save(self.filename)

if __name__ == '__main__':
    opers = OpeExcel()
    print(opers.get_lines())
    print(opers.get_value(3, 2))
