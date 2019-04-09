import socket

sk = socket.socket()
address = ('127.0.0.1',8000)
sk.connect(address)
while True:
    inp = input(">>>")
    sk.sendall(bytes(inp,'utf8'))
    res_len = int(str(sk.recv(1024),'utf8'))
    print(res_len)
    data = bytes()
    while len(data) != res_len:
        res = sk.recv(1024)
        data += res
    print(str(data,'gbk'))