'''import socket
a=socket.socket()
a.bind(('127.0.0.1', 35543))
a.listen(4)
print("this is listening")
while True:
    c,addr=a.accept()
    print("connecting from ",addr)
    s=input('enter the message:')
    c.send(s.encode())
    c.close()'''

import socket
s=socket.socket()
s.bind(('127.0.0.1',23476))
s.listen(2)
print("socket is connected")
c,addr=s.accept()
print("thank you for accepting",addr)
c.send(b'iam a socket')
print("message passed")
c.close()
s.close()    



