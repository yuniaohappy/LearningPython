class Bar:
    def __init__(self):
        print("Hello Bar!!")

# b = Bar()
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show(self):
        print("%s-%s" % (self.name,self.age))
lipeng = Person
lipeng("lipeng",19).show()
