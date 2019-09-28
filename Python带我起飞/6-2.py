

li = ['lipeng','32']

def recoder(person):
    person[0] = 'sss'
    print('姓名：',person[0],'年龄：',person[0])

recoder(li)
print(li)

# 元组类型不支持修改
# l2 = ['lipeng','32']
# def recoder2(*person):
#     person[0] = 'jjjj'
#     print('姓名：',person[0],'年龄：',person[0])
# recoder2(*l2)
# print(l2)

# reduce函数实现加和
y = lambda m,n:m + n
print(y(1,2))
from functools import reduce
print(reduce(lambda x,y:x + y,range(1,101)))

# map函数
t = map(lambda x:x ** 2,[1,2,3,4,5])
print(t)
print(list(t))

# filter函数
f = filter(lambda x:x % 2 == 0,[0,1,2,3,4,5,6,7,8,9])
print(f)
print(list(f))

from functools import partial
def f(name,age):
    print('姓名：',name,'年龄：',age)

p = partial(f,name='lipeng')
p(age = 32)

print(exec('1 + 2'))
print(eval('2 + 3'))

a = 10
b = 20
c = 30

g = {'a':6,'b':8}
t = {'b':100,'c':10}
print(eval('a + b + c',g,t))

