# UDP Socket CLIENT
import socket
port = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('127.0.0.1',port))
while True:
    data, addr = s.recvfrom(1024)
    print("Message: ", data.decode())
    print("From: ", addr)
    break


# UDP Socket SEND MESSAGE ONLY
import socket
port = 1234
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(b'Hello from client', ('127.0.0.1', port))
s.close()