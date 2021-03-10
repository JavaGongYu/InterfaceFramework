#!/usr/bin/env python
# encoding: utf-8
'''
@author: GongYu
@license: (C) Copyright 2020
@contact: gong_yu_1996@163.com
@software: PyCharm
@file: ConfigFile.py
@time: 2020/8/20 10:03
@desc: 配置文件，配置公共参数
'''

# 全局变量
HOST = 'https://bizapi.jd.com/api' # 网址
WorkBookName = '../data/JDDataExcel.xls' # 测试用例
SheetName = 'URL' # sheet表名
Token = '' # Token获取

# 邮箱信息
# 第三方 SMTP 服务
mail_host = "smtp.163.com"  # 设置服务器
mail_user = "gong_yu_1996@163.com"  # 用户名
mail_pass = "OICRHJRGCHSPAAIZ"  # 口令
sender = 'gong_yu_1996@163.com' # 发送邮箱
receivers = ['gong_yu_1996@163.com','1196936134@qq.com']  # 接收邮件邮箱，可设置为你的QQ邮箱或者其他邮箱
# 其他配置信息请修改EmailTool.py文件

# 数据库信息