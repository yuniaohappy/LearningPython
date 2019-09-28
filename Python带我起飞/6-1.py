# print('\n'.join([''.join([('ILovePython'[(x-y)%len('ILovePython')] if ((x * 0.05)**2 + (y*0.1)**2-1)**3 - (x*0.05)**2*(y*0.1)**3 <= 0 else ' ')for x in range(-32,32)])for y in range(17,-17,-1)]))
#
# print('\n'.join([''.join([('ILovePython'[(x-y)%len('ILovePython')]if((x*0.05)**2+(y*0.1)**2-1)**3-(x*0.05)**2*(y*0.1)**3<=0 else' ')for x in range(-32,32)])for y in range(17,-17,-1)]))

# 打印空心形图案
import math
def comparefu2(x,y):
    var3 = abs(y) - 0.65 * x * x
    return var3 >= 0.2
def comparefu1(x,y):
    H = 3
    var1 = math.sqrt(x * x + y*y) - H * math.sin(2 * math.atan(y / x))
    var2 = math.sqrt(x * x + y * y) - H * math.sin(2 * math.atan(-y / x))
    return abs(var1) <= 1 or abs(var2) <= 1

def printstar(y,stepy,comparefun):
    while(y <= 0):
        x = -4
        while(x <= 4):
            if comparefun(x,y):
                print('*',end='')
            else:
                print(' ',end='')
            x += 0.2
        y += stepy
        print("")
printstar(-4,0.2,comparefu1)
printstar(-1,0.2,comparefu2)

def recoder(name,age):
    if not isinstance(age,(int,str)):
        raise TypeError('类型错误')
    print('name:',name,'age:',age)

recoder('lipeng',34)

def recoder2(arg):
    arg.append(3)
x = [1,2]
recoder2(x)
print(x)

