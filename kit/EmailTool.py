#!/usr/bin/env python
# encoding: utf-8
'''
@author: GongYu
@license: (C) Copyright 2020
@contact: gong_yu_1996@163.com
@software: PyCharm
@file: EmailTool.py
@time: 2020/8/20 11:32
@desc: 发送邮件工具
'''

import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.header import Header
from config.ConfigFile import mail_host, WorkBookName
from config.ConfigFile import mail_user
from config.ConfigFile import mail_pass
from config.ConfigFile import sender
from config.ConfigFile import receivers
class SendEmail():
    def Email(slef):
        NewTime = time.strftime("%Y-%m-%d %H:%M")
        message = MIMEMultipart()
        #message['From'] = Header("GongYu", 'utf-8')
        message['To'] = Header("GongYu", 'utf-8')
        subject = '['+NewTime+']接口自动化测试报告'
        message['Subject'] = Header(subject, 'utf-8')

        # 邮件正文内容
        message.attach(MIMEText(
            '附件内容为《'+WorkBookName[8:][:-4]+'》接口自动化测试报告。测试时间为：'+NewTime+',请下载查看！\n'
            '运行Allure测试报告，需先安装Allure环境，相关文件请下载压缩包。',
            'plain', 'utf-8'))

        # 附件
        att1 = MIMEText(open(WorkBookName, 'rb').read(), 'base64', 'utf-8')
        att1["Content-Type"] = 'application/octet-stream'

        att1["Content-Disposition"] = 'attachment; filename="DataExcel.xls"'
        message.attach(att1)

        att2 = MIMEText(open('../report/Report.zip', 'rb').read(), 'base64', 'utf-8')
        att2["Content-Type"] = 'application/octet-stream'
        att2["Content-Disposition"] = 'attachment; filename="Report.zip"'
        message.attach(att2)
        try:
            smtpObj = smtplib.SMTP()
            smtpObj.connect(f'{mail_host}', 25)  # 25 为 SMTP 端口号
            smtpObj.login(f'{mail_user}', f'{mail_pass}')
            smtpObj.sendmail(f'{sender}',receivers, message.as_string())
            print("邮件发送成功!")
        except smtplib.SMTPException:
            print("Error: 邮件发送失败！")