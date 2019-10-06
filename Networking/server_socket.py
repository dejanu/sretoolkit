import socket

## SOCKETS method of creating a connection between processes
## sockets method of Inter-process communication to send message across network

## SERVER Implementationthat binds itself to a specific address and port
## and starts listening for incoming TCP communication

## test the server using netcat as client: nc <IP> <PORT>

SRV_ADDR = input("Type server IP: ")
SRV_PORT = int(input("Type sever PORT:"))

#create socket using AF_INET domain, Adress Family format is host and port no
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind the socket to the specified address and port
s.bind((SRV_ADDR, SRV_PORT))

#specify the max no of queued connection
s.listen(1)

print("Server started, waiting for connections ....")

# connection-socket obj,  address-client address bound to the socket
connection, address = s.accept()
print("Client connected with addr {}".format(address))

while 1:

    data = connection.recv(1024)
    if not data: break
    # message sent to client                 
    connection.sendall(b'---msg received-- ')
    print(data.decode())
          
connection.close()
