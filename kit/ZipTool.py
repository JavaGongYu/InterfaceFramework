#!/usr/bin/env python
# encoding: utf-8
'''
@author: GongYu
@license: (C) Copyright 2020
@contact: gong_yu_1996@163.com
@software: PyCharm
@file: ZipTool.py
@time: 2020/8/20 11:31
@desc: 压缩文件夹工具
'''
import os
import zipfile
import shutil
from kit.FileDispose import Files
from kit.Plan import Plans
class FileZip():
    def File(self,source_dir, output_filename):# 打包目录为zip文件（未压缩）
        Files().ZipFile()
        zipf = zipfile.ZipFile(output_filename, 'w')
        pre_len = len(os.path.dirname(source_dir))
        for parent, dirnames, filenames in os.walk(source_dir):
            for filename in filenames:
                pathfile = os.path.join(parent, filename)
                arcname = pathfile[pre_len:].strip(os.path.sep)  # 相对路径
                zipf.write(pathfile, arcname)
        zipf.close()
        shutil.move('Report.zip', '../report')
        print('报告打包完成，正在发送报告......')



