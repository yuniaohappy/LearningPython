# class MyClass:
#     __Occupation = 'scientist'
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#
#     def getrecode(self):
#         return self.name,self.age
#
#     def getoccupation(self):
#         return self.__Occupation
#
#     @property
#     def Occupation(self):
#         return self.__Occupation
#
# myc = MyClass('Anna',34)
# # myc.__Occupation = 'lipeng'
# # print(myc.__Occupation)
# # print(myc.getoccupation())
# # print(MyClass.__dict__)
# # print(myc._MyClass__Occupation)
# print(myc.getoccupation())
# print(myc.Occupation)

class MyClass:
    __Occupation = 'scientist'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @property
    def Occupation(self):
        return self.__Occupation
    @Occupation.setter
    def Occupation(self,value):
        if (value != 'inventor') and (value != 'scientist'):
            raise (ValueError('Occupation must be inventor or scitentist'))
        else:
            self.__Occupation = value

myc = MyClass('Anna',42)
print(myc.Occupation)
myc.Occupation = 'inventor'
print(myc.Occupation)

