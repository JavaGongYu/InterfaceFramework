#!/usr/bin/env python
# encoding: utf-8
'''
@author: GongYu
@license: (C) Copyright 2020
@contact: gong_yu_1996@163.com
@software: PyCharm
@file: LoginDemo.py
@time: 2020/8/20 11:29
@desc: 登录类(应用获取Token)
'''
import hashlib
import time
from demo.DemoMain import RunMain

class LoginClass():
    def MD5DataL(self,pwd): # 密码加密
        md5 = hashlib.md5()
        md5.update(pwd.encode('utf-8'))
        return md5.hexdigest()

    def MD5DataA(self,data): # 签名生成
        md5 = hashlib.md5()
        md5.update(data.encode('utf-8'))
        return md5.hexdigest().upper()

    def Login(self): # 登录
        NewTime = time.strftime("%Y-%m-%d %H:%M:%S") # 获取时间
        pwd = LoginClass().MD5DataL('123456') # 密码加密
        sign = 'client_secret'+NewTime+'client_id'+'username'+pwd+'access_token' # 生成签名
        MD5sign = LoginClass().MD5DataA(sign) # 签名加密
        url = 'https://bizapi.jd.com/oauth2/accessToken'
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        data = {
            'grant_type': 'access_token',
            'client_id': 'client_id',
            'timestamp': NewTime,
            'username': 'username',
            'password': LoginClass().MD5DataL('123456'),
            'sign': MD5sign
        }
        Res = RunMain().run_main(url=url, method="POST", params=data, headers=headers)
        return Res.json()['result']

