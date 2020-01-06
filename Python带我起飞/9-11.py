#Python中元类的实现原理
# def fun(self):
#     print('元类中的函数！！！')
#
# # cls = type('MyClass',(object,),dict(myfun=fun))
# cls = type('MyClass',(object,),{'myfun':fun})
# obj = cls()
# obj.myfun()
# print(cls.__name__)
# print(cls.__bases__)
# print(cls.__dict__)

class MyClassMetaClass(type):
    def __new__(cls, name, bases,attrs):
        attrs['add'] = lambda self,value:print('add value %s '%value)
        attrs['name'] = 'personName'
        return type.__new__(cls,name,bases,attrs)

class MyClass(object,metaclass=MyClassMetaClass):
    pass
obj = MyClass()
obj.add(55)
print(obj.name)


