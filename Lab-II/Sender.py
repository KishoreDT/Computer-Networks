import socket
LOCALHOST = "127.0.0.1"
PORT = 8080
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((LOCALHOST, PORT))
server.listen(1)
print("Server started")
print("Waiting for client request..")
while True:
    clientConnection,clientAddress = server.accept()
    print("Connected clinet :" , clientAddress)
    data = clientConnection.recv(1024)
    print("From Client :" , data.decode())
    clientConnection.send(bytes("Hi, Hello, I'm Kishore DT",'UTF-8'))
    clientConnection.close()