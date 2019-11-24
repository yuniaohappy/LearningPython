

# li = ['lipeng','32']
#
# def recoder(person):
#     person[0] = 'sss'
#     print('姓名：',person[0],'年龄：',person[0])
#
# recoder(li)
# print(li)
#
# # 元组类型不支持修改
# # l2 = ['lipeng','32']
# # def recoder2(*person):
# #     person[0] = 'jjjj'
# #     print('姓名：',person[0],'年龄：',person[0])
# # recoder2(*l2)
# # print(l2)
#
# # reduce函数实现加和
# y = lambda m,n:m + n
# print(y(1,2))
# from functools import reduce
# print(reduce(lambda x,y:x + y,range(1,101)))
#
# # map函数
# t = map(lambda x:x ** 2,[1,2,3,4,5])
# print(t)
# print(list(t))
#
# # filter函数
# f = filter(lambda x:x % 2 == 0,[0,1,2,3,4,5,6,7,8,9])
# print(f)
# print(list(f))

# from functools import partial
# def f(name,age):
#     print('姓名：',name,'年龄：',age)
#
# p = partial(f,name='lipeng')
# p(age = 32)
#
# print(exec('1 + 2'))
# print(eval('2 + 3'))
#
# a = 10
# b = 20
# c = 30
#
# g = {'a':6,'b':8}
# t = {'b':100,'c':10}
# print(eval('a + b + c',g,t))
import logging

logging.basicConfig(filename='test.log',filemode='w',level=logging.INFO,format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger(__name__)


# 字符串转换为组合对象
def StringToOther(s):
    b = eval(s)
    logger.info("b is {}".format(b))
    logger.warning("b is {}".format(b))
    logger.error("b is {}".format(b))
    return b
# 组合对象转换为字符串
def OtherToString(o):
    b = repr(o)
    return b

# 列表转换
# def fun1():
#     a = "[[1,2],[3,4],[5,5],[7,8],[9,10]]"
#     b = StringToOther(a)
#     c = OtherToString(b)
#     print(b,'\ttype:',type(b))
#     print(c,'\ttype:',type(c))
# # 字典转换
# def fun2():
#     a = "{1:'a',2:'b'}"
#     b = StringToOther(a)
#     c = OtherToString(b)
#     print(b, '\ttype:', type(b))
#     print(c, '\ttype:', type(c))
# # 元组转换
# def fun3():
#     a = "([1,2],[3,4],[5,5],[7,8],[9,10])"
#     b = StringToOther(a)
#     c = OtherToString(b)
#     print(b, '\ttype:', type(b))
#     print(c, '\ttype:', type(c))

# if __name__ == '__main__':
#     s = ''
#     for k in range(1,4):
#         s += 'fun' + str(k) + '()\n'
#     exec(s)
#
# # mylist = [x * x for x in range(3)]
# # for i in mylist:
#     print(i)
# print(mylist)
#
# mygen = (x * x for x in range(3))
# for i in mygen:
#     print(i)
# print(mygen)

# var = 1
# def fun1():
#     # var = 2
#     def fun2():
#         global var
#         var = 3
#         print(var)
#     fun2()
# fun1()
# print(var)
# import builtins
# print(dir(builtins))

a = 6
def func():
    a = 7
    def nested():
        nonlocal a
        a += 1
    nested()
    print('本地',a)
func()
print('全局',a)


