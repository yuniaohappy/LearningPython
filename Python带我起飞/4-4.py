# int1 = -5
# int2 = -5
# print(id(int1),id(int2))

# s1 = "李昕睿"
# s2 = "李昕睿"
# print(id(s1),id(s2))

# int3 = 257
# int4 = 257
# print(id(int3),id(int4))

# f1 = 256.4
# f2 = 256.4
# print(id(f1),id(f2))
# f1 = -2.45
# # f2 = -2.45
# # print(id(f1),id(f2))

# int1 = -7
# int2 = -7
# print(id(int1),id(int2))

a,b,c = 3,5,None
print(a < b and c is None,'\a')

print('{0:=>10d}'.format(5))
print('{0:&<10.3f}'.format(0.5))
print('{0:-^10}'.format('hello'))
print('{hello:-^10}'.format(hello='hello'))