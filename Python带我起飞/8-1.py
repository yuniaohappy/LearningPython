import os,sys
# print(sys.version)
# print(sys.api_version)
# f = open('a.txt','wb+')
# print(f.write(b'lipeng'))
# f.close()
# os.remove('a.txt')
# for o in os.environ:
#     print(o)

try:
    f = os.open('a.txt','wb+')
    f.write('lipeng')
except Exception as e:
    print(e)
    f.write(b'lipeng')
finally:
    print('关闭文件')
    f.close()
try:
    f = open('a.txt','r+')
    print(f)
    for line in f:
        print(line)
finally:
    f.close()
