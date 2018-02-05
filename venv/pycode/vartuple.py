# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 21:01
# @Author  : huxuanhua
# @Email   : huxhua163@163.com
# @File    : vartuple.py
# @Software: PyCharm
def printinfo(arg1, *vartuple):
    print '输出:'
    print arg1
    for var in vartuple:
        print var
    return

printinfo(10)
printinfo(70,20,3)