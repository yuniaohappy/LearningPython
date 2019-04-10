# # gevent 下的协程
# from gevent import Greenlet as greenlet
#
# def test1():
#     print(12)
#     gr2.switch()
#     print(34)
#     gr2.switch()
#
# def test2():
#     print(56)
#     gr1.switch()
#     print('00000')
#     print(78)
#
# gr1 = greenlet(test1)
# gr2 = greenlet(test2)
# gr1.switch()

from urllib.request import urlopen
resp = urlopen('http://www.baidu.com')
data = resp.read()
print(data)
