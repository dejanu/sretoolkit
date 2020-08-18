#!/usr/bin/python

import socket
import sys

print(sys.version)

if sys.version_info[0] ==3:
	target = input("Enter the IP address to scan: ")
	portrange = input("Enter port-range eg. 5-200: ")
else:
	target = raw_input("Enter the IP address to scan: ")
	portrange = raw_input("Enter port-range eg 5-200: ")


first_port = int(portrange.split('-')[0])
last_port = int(portrange.split('-')[-1])


print("Scanning host {0}, from port {1} to port {2}".format(target,first_port,last_port))

for p in range(first_port, last_port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    status = s.connect_ex((target,p))
    if (status == 0):
        print("PORT {} open ".format(p))
    else:
        print("PORT {} close ".format(p))
    s.close()
