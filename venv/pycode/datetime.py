# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 20:38
# @Author  : huxuanhua
# @Email   : huxhua163@163.com
# @File    : datetime.py
# @Software: PyCharm
import datetime

i = datetime.datetime
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat())
print ("当前的年份是 %s" % i.year)
print ("当前的月份是 %s" % i.month)
print ("当前的日期是  %s" % i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year))
print ("当前小时是 %s" % i.hour)
print ("当前分钟是 %s" % i.minute)
print ("当前秒是  %s" % i.second)
