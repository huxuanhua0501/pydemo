# -*- coding: utf-8 -*-
# @Time    : 2018/2/2 19:46
# @Author  : huxuanhua
# @Email   : huxhua163@163.com
# @File    : variable.py
# @Software: PyCharm
# 变量---全局 ,局部
total = 0


def sum(arg1, arg2):
    total = arg1 + arg2
    print total
    return total


sum(10, 19)
print total
