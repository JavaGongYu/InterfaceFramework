'''
* encoding:utf-8 *
@author: GongYu
@license: (C) Copyright 2021
@contact: gong_yu_1996@163.com
@software: PyCharm/Python3.7
@file: Log.py
@time: 2021/3/8 17:52
@desc: 日志类
'''
import os
import sys
import time


class Logger(object):
    def __init__(self, stream=sys.stdout):
        output_dir = "../log"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        log_name = '{}.log'.format(time.strftime('%Y_%m_%d_%H_%M'))
        filename = os.path.join(output_dir, log_name)

        self.terminal = stream
        self.log = open(filename, 'a+')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass