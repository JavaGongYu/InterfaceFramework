'''
* encoding:utf-8 *
@author: GongYu
@license: (C) Copyright 2021
@contact: gong_yu_1996@163.com
@software: PyCharm/Python3.7
@file: FileDispose.py
@time: 2021/3/9 10:30
@desc: 文件处理类，判断文件是否存在等操作
'''
import os
import shutil
from kit.Plan import Plans
class Files():
    def ReportsFile(self):
        if os.path.exists('../report/xml') == True or os.path.exists('../report/html') == True:
            print("报告目录存在！正在执行删除",end='')
            Plans().Plan()
            shutil.rmtree(r'../report/xml')
            shutil.rmtree(r'../report/html')
            if os.path.exists('../report/xml') == False or os.path.exists('../report/html') == False:
                print("删除成功！")
            else:
                print('删除失败，正在重新删除',end='')
                Plans().Plan()
                while os.path.exists('../report/xml') == True or os.path.exists('../report/html') == True:  # 循环删除
                    shutil.rmtree(r'../report/xml')
                    shutil.rmtree(r'../report/html')
                print('删除成功！')
        else:
            pass  # 跳过直接运行下方代码

    def ZipFile(self):
        if os.path.exists('../report/Report.zip') == True :
            print("报告压缩文件存在！正在执行删除",end='')
            Plans().Plan()
            os.remove('../report/Report.zip')
            while os.path.exists('../report/Report.zip') == True :
                print('删除失败！正在重新删除',end='')
                Plans().Plan()
                os.remove('../report/Report.zip')
            print("删除成功！正在执行打包操作",end='')
            Plans().Plan()
        else:
            print('正在执行打包操作',end='')
            Plans().Plan()