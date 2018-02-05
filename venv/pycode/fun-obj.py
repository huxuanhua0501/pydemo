# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 20:51
# @Author  : huxuanhua
# @Email   : huxhua163@163.com
# @File    : fun-obj.py
# @Software: PyCharm
def changeme(mylist):
    mylist.append([1, 2, 3, 4])
    print '函数内取值:', mylist
    return


mylist = [10, 20, 30]
changeme(mylist)
print '函数外取值:', mylist
