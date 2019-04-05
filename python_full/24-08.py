class F:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def f1(self):
        print("F.f1")
    def f2(self):
        print("F.f2")

class S(F):
    def s1(self):
        print("S.s1")
    def f2(self):
        print("S.f2",self.name,self.age)
        # super(S,self).f2()
        F.f2(self)

def d():
    print("d")

s = S("name","age")
# s.f1()
# s.s1()
s.f2()