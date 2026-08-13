import socket
s=socket.socket()
print("client is connected")
s.connect(('127.0.0.1',34567))
data=s.recv(1024)
print("message is received",data.decode())

