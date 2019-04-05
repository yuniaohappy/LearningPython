import socket

sk = socket.socket()
print(sk)
sk.connect(('127.0.0.1',8000))
# sk.send()
sk.sendall(bytes("中国",'utf8'))