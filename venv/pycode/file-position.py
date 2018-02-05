# -*- coding: utf-8 -*-
# @Time    : 2018/2/2 20:47
# @Author  : huxuanhua
# @Email   : huxhua163@163.com
# @File    : file-position.py
# @Software: PyCharm
# 打开一个文件
fo = open('foo.txt', 'r+')
str = fo.read(11)
print str
# 查找当前位置
position = fo.tell()
print position
fo.closed
