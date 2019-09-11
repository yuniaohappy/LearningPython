"""
利用for循环实现冒泡排序
"""

s = [5,8,20,1]
print(s)
for m in range(len(s) - 1):
    for n in range(len(s) - 1):
        if s[n] > s[n + 1]:
            s[n],s[n + 1] = s[n + 1],s[n]
print(s)