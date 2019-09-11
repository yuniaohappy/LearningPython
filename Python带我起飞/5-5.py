"""
打印九九乘法表
"""

for x in range(1,10):
    for y in range(1,x+1):
        print(y ,"x",x,'=',x*y,'\t',end='')
    print()
