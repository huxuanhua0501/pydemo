# -*- coding: utf-8 -*-
# @Time    : 2018/2/2 21:31
# @Author  : huxuanhua
# @Email   : huxhua163@163.com
# @File    : try-finally.py
# @Software: PyCharm
try:
    f = open('E:\\xxx.txt', 'r')
    print f.read()
finally:
    if f:
        f.close()