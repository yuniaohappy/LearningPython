class Record:
    __slots__ = ('name','age')

rec = Record()
rec.name = 'Anna'
rec.age = 34
# rec.sex = '男'

print('name: ',rec.name,'age: ',rec.age)

# class MyClass:
#     def f(self):
#         return 'I Love Python'
#     @classmethod
#     def fcls(cls):
#         return '类方法：CLS'
#     @staticmethod
#     def fstatic():
#         return '静态方法：static'
#
# myc = MyClass()
# print(myc.f())
# print(myc.fcls())
# print(MyClass.fcls())
# # print(MyClass.f())
# print(MyClass.fstatic())
# print(myc.fstatic())

class MyClass:
    Occupation = 'scientist'
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def getrecode(self):
        return self.name,self.age
    def __del__(self):
        print(self.__class__.__name__,'DEL')
myc = MyClass('Anna',42)
myc2 = MyClass('Gary',38)
myc2.Occupation = 'inventor'
# myc.Occupation = 'lipeng'
# del myc
MyClass.Occupation = 'dancer'
# print(myc.Occupation)
print(myc2.Occupation)

