import socket

## SOCKET method (protocol agnostic) of creating a communication between processes
## socket methods of Inter-process communication to send messages across a network

## CLIENT implementation that connect to a socket and sends data
## eg: nc <IP> <PORT>


SRV_ADDR = input("Connect to IP: ")
SRV_PORT = int(input("Using PORT: "))


def read_message(msg=None):
    """read from stdin and send to server"""

    if not msg:
        msg = input("Type message to be send: ")
    else:
        pass

    #convert from str to bytes
    return msg.encode()
    

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((SRV_ADDR,SRV_PORT))
    
    #send data to server test message
    #s.sendall(b'Hello world..')
    message =  read_message("Pass a string maan")
    s.sendall(message)
    
    #read message from server and choose the buffer size
    data = s.recv(1024)


print("Received", repr(data))


