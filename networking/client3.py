import socket
s=socket.socket()
print("socket is connected")
s.connect(('127.0.0.1',34567))
data=s.recv(1024)
print("message accepted:",data.decode())
