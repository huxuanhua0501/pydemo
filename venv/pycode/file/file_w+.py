# -*- coding: utf-8 -*-
# @Time    : 2018/2/2 21:15
# @Author  : huxuanhua
# @Email   : huxhua163@163.com
# @File    : file_w+.py
# @Software: PyCharm
import os

document = open('E:\\testfile.txt', 'w+')
print '文件名字:', document
document.write('这是我创建的第一个python文件')
print document.tell()
# 输出当前指针位置
document.seek(os.SEEK_SET)
# 设置指针为原始位置
context = document.read()
print context
document.closed
