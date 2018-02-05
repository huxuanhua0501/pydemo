# -*- coding: utf-8 -*-
# @Time    : 2018/2/2 19:48
# @Author  : huxuanhua
# @Email   : huxhua163@163.com
# @File    : global.py
# @Software: PyCharm
globvar = 0


def set_global_to_one():
    global globvar
    globvar = 1


print globvar

set_global_to_one()
print globvar
