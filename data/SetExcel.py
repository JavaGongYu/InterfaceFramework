#!/usr/bin/env python
# encoding: utf-8
'''
@author: GongYu
@license: (C) Copyright 2020
@contact: gong_yu_1996@163.com
@software: PyCharm
@file: SetData.py
@time: 2020/8/20 10:58
@desc: 响应数据写入Excel
'''
import os
import xlrd
import json
from xlutils import copy
from config.ConfigFile import WorkBookName
from config.ConfigFile import SheetName
class CSetExcel():
    def SetExcel(self,infodata,one,Col=10):
        try:
            path = f'{WorkBookName}'
            workSheet = xlrd.open_workbook(path,formatting_info=True)
            New_workSheet = copy.copy(workSheet) # 复制表格
            New_Sheet = New_workSheet.get_sheet(f'{SheetName}') # 获取表格名
            New_Sheet.write(one,Col,json.dumps(infodata,ensure_ascii=False)) # 写入Excel
            New_workSheet.save(path) # 保存
        except PermissionError:
            print('数据文件被打开，数据写入失败！程序关闭')
            os._exit(0)
