import socket
sk = socket.socket()
sk.bind(('127.0.0.1',8000))
print(sk)
sk.listen(3)
print("waiting......")
conn,addr = sk.accept()
print("conn:",conn,"addr:",addr)

print(str(conn.recv(1024),'utf8'))