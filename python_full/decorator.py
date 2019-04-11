def log(fun):
    def wrapper():
        print('日志：',fun.__name__)
        return fun()
    return wrapper

@log
def now():
    print('hello world')

now()
# def int2(x,base=2):
#     return int(x,base)

# print(int2('1000000'))
# print(int2('1010101'))
import functools
int2 = functools.partial(int,base=2)
print(int2('1000000'))
print(int2('1010101'))