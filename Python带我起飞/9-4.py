#类的继承
class Record:
    __Occupation = 'scientist'
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getOccupation(self):
        return self.__Occupation
    def showrecode(self):
        print('Occupation: ',self.getOccupation())

# class GirlRecord(Record):
#     def showrecode(self):
#         # Record.showrecode(self)
#         super().showrecode()
#         print('name: ',self.name,'age: ',self.age)
#
# myc = GirlRecord('Anna',45)
# myc.showrecode()

class FemaleRecode(Record):
    def showrecode(self):
        print(self.name,':',self.age,';female')
        super().showrecode()

class RetireRecord(Record):
    def showrecode(self):
        super().showrecode()
        print('retired worker')

class ThisRecord(FemaleRecode,RetireRecord):
    def showrecode(self):
        print('the member detail as follow: ')
        super().showrecode()
        # FemaleRecode.showrecode(self)
        # RetireRecord.showrecode(self)

myc = ThisRecord('Anna',32)
myc.showrecode()

# print(isinstance(myc,Record))
# print(issubclass(ThisRecord,int))

print(getattr(myc,'name'))
setattr(myc,'name','lipeng')
print(myc.name)
