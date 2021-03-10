#!/usr/bin/env python
# encoding: utf-8
'''
@author: GongYu
@license: (C) Copyright 2020
@contact: gong_yu_1996@163.com
@software: PyCharm
@file: DemoMain.py
@time: 2020/8/20 11:26
@desc: 公共请求主类
'''
import requests

class RunMain:
    def __init__(self):
        pass

    @staticmethod
    def send_post(url,cookies,headers,params=None):
        try:
            res = requests.post(url=url,cookies=cookies,headers=headers,data=params)
            return res #在断言处可自行获取返回值内容
            #return res.status_code # 返回响应状态代码
        except Exception as msg:
            print(msg) # 打印错误信息
            return msg

    @staticmethod
    def send_get(url,cookies,headers,params=None,):
        try:
            res = requests.get(url=url,cookies=cookies,headers=headers,params=params,)
            return res  # 在断言处可自行获取返回值内容
            # return res.status_code # 返回响应状态代码
        except Exception as msg:
            print(msg) # 打印错误信息
            return msg

    def run_main(self, url,method,cookies=None,headers=None,params=None):
        if method == 'GET':
            res = self.send_get(url,cookies,headers,params)
            return res
        elif method == 'POST':
            res = self.send_post(url,cookies,headers,params)
            return res
        else:
            return '不支持的请求方式！'

