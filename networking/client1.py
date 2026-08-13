import socket
s=socket.socket()
print("client is connected")
while True:
    s.connect(('127.0.0.1',23476))
    data=s.recv(1024)
    print("chat is received",data.decode())
    hlo=input("msg to:")
    s.send(hlo.encode())
    s.close()
