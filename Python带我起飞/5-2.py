"""
将十进制转换为二进制数
"""

a = input("请输入一个十进制数：")
d = int(a.strip())
s = ""
while d != 0:
    d,f = divmod(d,2)
    s = str(f) + s
print(s)

words = ['I','love','Python']
for item in words[:]:
    words.insert(0,item)
    print(item)
print(words)

