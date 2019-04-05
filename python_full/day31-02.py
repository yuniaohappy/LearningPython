s = '苑昊'
# print(type(s))
b1 = s.encode('utf8')
b2 = s.encode('gbk')
print(b1,type(b1))
print(b1,type(b2))
# b2 = b1.decode('utf8')
b3 = b2.decode('gbk')
print(b3,type(b3))