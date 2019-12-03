#装饰器实现原理
def checkParams(fn):
    def wrapper(name):
        if isinstance(name,str):
            return fn(name)
        print('参数类型不正确！！！')
        return None
    return wrapper
def wrapperfun(name):
    def recoder(age):
        print('姓名：',name,'姓名：',age)
    return recoder

wrapperfun2 = checkParams(wrapperfun)
fun = wrapperfun2('Anna')
fun(37)






#闭包的实现过程
# def recoder(name,age):
#     print('姓名：',name,'年龄：',age)
# def Garyfun(age):
#     name = 'Gary'
#     return recoder(name,age)
# Garyfun(32)
# def Annafun(age):
#     name = 'Anna'
#     return recoder(name,age)
# Annafun(20)
#
# def wrapperfun(name):
#     def recoder(age):
#         print('姓名：',name,'年龄：',age)
#     return recoder
# fun = wrapperfun('Gary')
# print(fun.__closure__)
# fun(32)
#
# fun1 = wrapperfun('Anna')
# fun1(20)
