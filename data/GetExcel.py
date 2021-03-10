#!/usr/bin/env python
# encoding: utf-8
'''
@author: GongYu
@license: (C) Copyright 2020
@contact: gong_yu_1996@163.com
@software: PyCharm
@file: GetExcel.py
@time: 2020/8/20 10:12
@desc: 读取Excel表格数据
'''
import xlrd
from config.ConfigFile import WorkBookName
from config.ConfigFile import SheetName

def get_excel_data(): # 获取数据函数
    data = xlrd.open_workbook(f'{WorkBookName}').sheet_by_name(f'{SheetName}') # 打开表格
    user_data = [] # 生成一个空列表
    for i in range(1, data.nrows):
        dv = data.cell(i, 12).value
        if dv == 'Yes' or dv == 'yes' or dv == 'y':  # 判断是否读取
            user_data.append((data.row_values(i)))  # 追加到列表
        else:
            pass

    return user_data # 返回数据列表
