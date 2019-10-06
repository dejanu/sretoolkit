import socket


target = input("Enter the IP address to scan: ")
portrange = int("Enter port-range eg 5-200: ")

first_port = int(portrange.split('-')[0])
last_port = int(portrange.split('-')[-1])


print("Scanning host {}, from port {1} to port {2}".format(target,first_port,last_port))


from p in range(first_port, last_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target,port))
    if (status == 0):
        print("PORT {} open ".format(port))
    else:
        print("PORT {} close ".format(port))
    s.close()
