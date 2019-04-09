# class F1:
#     def f(self):
#         print("F1.f")
#
# class F2:
#     def f(self):
#         print("F2.f")
#
# class S(F2,F1):
#     pass
#
# s = S()
# s.f()
class Test1:
    def d1(self):
        print("Test1.d1")
    def d2(self):
        print("Test1.d2")
class Test2:
    def t1(self):
        print("Test2.t1")
        self.t2()
    def t2(self):
        print("Test2.t2")

class Test3(Test1,Test2):
    def t2(self):
        print("Test3.t2")

t = Test3()
t.t1()