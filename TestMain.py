#!/usr/bin/env python
# encoding: utf-8
'''
@author: GongYu
@license: (C) Copyright 2020
@contact: gong_yu_1996@163.com
@software: PyCharm
@file: TestMain.py
@time: 2020/8/21 15:05
@desc: 运行主类
'''
import shutil
import pytest
import os

from kit.FileDispose import Files
from kit.Plan import Plans
from kit.ZipTool import FileZip
from kit.EmailTool import SendEmail

if __name__ == '__main__':  # 启动allure
    Files().ReportsFile()
    print('正在执行测试用例')
    pytest.main(['../test_case/Test_Case.py', '-s', '--alluredir', '../report/xml'])
    print('测试用例执行完成')
    print('正在转换测试报告', end='')
    Plans().Plan()
    os.system('allure generate ../report/xml -o ../report/html')  # 测试报告文件转HTML
    FileZip().File('../report', 'Report.zip')  # 打包报告
    SendEmail().Email()  # 调用方法 发送邮件
    print('正在启动测试报告......')
    os.system('allure serve ../report/xml')  # 运行测试报告文件