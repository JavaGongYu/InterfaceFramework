#!/usr/bin/env python
# encoding: utf-8
'''
@author: GongYu
@license: (C) Copyright 2020
@contact: gong_yu_1996@163.com
@software: PyCharm
@file: Test_Case.py
@time: 2020/8/20 14:49
@desc: 测试用例执行方法类
'''

import json
import pytest
import allure
from data.GetExcel import get_excel_data
from data.SetExcel import CSetExcel
from demo.DemoMain import RunMain
from config.ConfigFile import HOST
from config.ConfigFile import Token



@allure.feature('接口测试') #allure注解
class Testapi():
    @allure.story('运行测试')
    @pytest.mark.parametrize('id,caseid,casename,casenote,url,method,headers,infodata,infodatanote,resultdata,actualdata,actualresults,yn',get_excel_data()) # 参数化
    def test_api(self,id,caseid,casename,casenote,url,method,headers,infodata,infodatanote,resultdata,actualdata,actualresults,yn):
        NewHeaders = json.loads(headers)  # 字符串转换字典
        NewHeaders['token'] = f'{Token}'  # 新增Token到字典中
        if infodata == '':
            """
            判断参数是否为空，如果参数为空，则不转换
            如不判断，参数为空报错
            """
            Res = RunMain().run_main(url=f'{HOST}' + url, method=method, headers=NewHeaders) # 发送请求
        else:
            data = json.loads(infodata) # 参数字符串转换字典
            Res = RunMain().run_main(url=f'{HOST}' + url, method=method, headers=NewHeaders,params=data) # 发送请求
        CSetExcel().SetExcel(Res.json(), json.loads(id)) # 返回数据写入Excel
        assert Res.status_code == 200 # 断言响应状态代码 考虑返回值是否为200 可写入Excel中读取
        # 断言响应值
        assert Res.json()['resultMessage'] == json.loads(resultdata)['resultMessage']
        assert Res.json()['success'] == json.loads(resultdata)['success']