import socket
import subprocess

sk = socket.socket()
address = ('127.0.0.1',8000)
sk.bind(address)
sk.listen(3)

while True:
    conn, addr = sk.accept()
    while True:
        res = str(conn.recv(1024),'utf8')
        cmd = subprocess.Popen(res,shell=True,stdout=subprocess.PIPE)
        data = cmd.stdout.read()
        res_len = len(data)
        print("len: ",res_len)
        conn.sendall(bytes(str(res_len),'utf8'))
        # print(cmd.stdout.read())
        conn.sendall(data)
