"""正则表达式"""
import re
r = re.search(r"r[au]n","dog runs to cat")
print(r)
print(r.group())

"""set找不同"""
# char_list = ['a','b','c','c','d','d','d']
# print(set(char_list))
# ch = set(char_list)
# ch.add('z')
# ch.pop()
# ch.remove('a')
# print(ch)
# set1 = {'a','m','b'}
# print(ch.difference(set1))

"""pickle存取数据"""
# import pickle
# a_dic = {'da':111,2:[3,4,5],'23':{1:'test'}}
# file = open("pickle_exp.pickle",'wb')
# pickle.dump(a_dic,file)
#
# with open("pickle_exp.pickle",'rb') as file2:
#     p = pickle.load(file2)
#     file2.close()
# print(p)

"""浅复制和深复制"""
# import copy
# a = [1,2,3]
# b = a
# print(id(b))
# print(id(a) == id(b))
# c = copy.copy(a)
# print(id(c))
# d = copy.deepcopy(a)
# print(id(d))


"""zip,lambda,map"""
# a = [1,2,3]
# b = [4,5,6]
# print(list(zip(a,b,b)))
# for i,j in zip(a,b):
#     fun = lambda x, y: x + y
#     print(fun(i,j))
#     print(i,"\t", j)
# fun1 = lambda x, y: x + y
# print(list(map(fun1,a,b)))


"""异常处理try"""
# try:
#     file = open("file",'r+')
# except Exception as e:
#     print("This file is not exist!")
#     a_file = input("Please create this file? ")
#     if a_file == 'y':
#         file = open("file", 'w')
#     else:
#         pass
# else:
#     file.write("Test File")
# file.close()

"""continue 和 break"""
# a = 0
# while True:
#
#     if a == 10:
#         print(a)
#         a += 1
#         continue
#     elif a == 20:
#         print(a)
#         a += 1
#         break
#     else:
#         print("PASS " + str(a))
#         a += 1

"""import """
# import time
# print(time)
# print(time.localtime().tm_mday,time.localtime().tm_mon)
# print(time.time())

"""字典"""
# dic = {}
# dic["apple"] = 5
# print(dic.items())
# print(dic["apple"])

"""多维列表"""
# a = [2, 4, [3, 4, 5, [2, 4, 3, 3]]]
# print(a[2][3][0])

"""列表"""
# a_list = [2,3,4,5,67,7,8,8,9,9]
# a_list.append(99)
# a_list.pop(4)
# a_list.insert(1,0)
# a_list.remove(9)
# a_list.sort(reverse=True)
# print(a_list.count(8))
# print(a_list.index(2))
# print(a_list[:])
# print(a_list[-5])
# print(a_list)

"""元组  列表"""
# a_tuple = (1, 2, 3, 4, 5, 6)
# another_tuple = 4, 5, 6, 7, 8
# a_list = []
# print(a_tuple[2])
# for tuple in range(1,6):
#     print(tuple,' + ',a_tuple[tuple])
# print(type(a_list))

"""input"""
# a_input = input("input number is :")
# a_input = int(a_input)
# if a_input == 1:
#     print("this is one!")
# elif a_input == 2:
#     print("this is two!")
# elif a_input == 3:
#     print("this is three")
# else:
#     print("input ERRO")
# print("this number is :", a_input)

# class Calculator:
#     name = "Calculator"
#     price = 18
#
#     def __init__(self,name,price):
#
#         self.name = name
#         self.price = price
#
#     def add(self, x, y):
#         result = x + y
#         print(result)
#         return result
#
# # cal = Calculator("Claculator_test",price=19)
# # cal.add(5, 6)
# # print(cal.name)
# # print(cal.price)
#
