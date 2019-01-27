#-*- encoding=utf-8 -*-
#生成器都是迭代器
# l = [1,2,3,4]
# print(l)
# print(iter(l))
# print(next(iter(l)))

#迭代器：1、有iter方法；2、有next方法
# for循环内部三件事儿：1、调用可迭代对象的iter方法返回一个迭代器对象；2、调用迭代器方法；3、处理StopIteration方法。
# from collections import Iterator,Iterable
# l = [1,2,3,4]
# d = iter(l)
# print(isinstance(l,list))
# print(isinstance(l,Iterable))
# #迭代器和生成器的区别
# with open("16-04.py",encoding="utf-8") as f:
#     l = sorted([len(x) for x in f.readlines()])[-1]
#     print(l)

import time
# print(help(time))
# print(time.time())
# print(time.clock())
# print(time.gmtime())
# print(time.localtime())
# print(time.asctime())
# print(time.ctime())
# print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))
# print(time.strptime("2019-01-27 18:40:46","%Y-%m-%d %H:%M:%S"))

import datetime
print(datetime.datetime.now())


