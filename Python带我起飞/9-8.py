class MyEpt(Exception):
    def __init__(self,value):
        self.value = value

    def __str__(self):
        return repr(self.value)

try:
    raise MyEpt('这是个自定义异常！！！')
except MyEpt as e:
    print(e.value)
