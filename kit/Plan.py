'''
* encoding:utf-8 *
@author: GongYu
@license: (C) Copyright 2021
@contact: gong_yu_1996@163.com
@software: PyCharm/Python3.7
@file: Plan.py
@time: 2021/3/9 10:52
@desc: 进度条工具
'''
import sys, time
class Plans():
    def Plan(self):
        for i in range(4):
            if i != 3:
                sys.stdout.write("..")
            else:
                pass
            sys.stdout.flush()
            time.sleep(0.5)
        print('')