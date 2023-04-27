# TCP Socket SEND MESSAGE ONLY
import socket 
s = socket.socket()
port = 1234
s.bind(('127.0.0.1', port))        
s.listen(5)
while True:
    c, addr = s.accept()
    c.send('Hello World'.encode())
    c.close()
    break

#  TCP Socket Client
import socket
s = socket.socket()
port = 1234
s.connect(('127.0.0.1',port))
print(s.recv(1024).decode())
s.close()