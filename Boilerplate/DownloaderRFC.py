import sys , urllib.request
import ssl


# Fix URLError urlopen error SSL: Certifiacte Verify FALSE, prereq pip install certi
try:
   _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    # Legacy Python that doesn't verify HTTPS certificates by default
    pass
else:
    # Handle target environment that doesn't support HTTPS verification
    ssl._create_default_https_context = _create_unverified_https_context


try:
	rfc_number = int(sys.argv[1])
except (IndexError, ValueError):
	print('Must supply RFCnumber as first argument')
	sys.exit(2)


template = 'http://www.ietf.org/rfc/rfc{}.txt'
url = template.format(rfc_number)
rfc_raw = urllib.request.urlopen(url).read()
rfc = rfc_raw.decode()
print(rfc)

######################Python2#######################
## using socket implementation of TCP UPD

# import sys,socket
# import ssl



# try:
# 	rfc_number = int(sys.argv[1])
# except (IndexError, ValueError):
# 	print("Must supply RFC as first argument")
# 	sys.exit(2)

# # tell socket which transport layer to use aka create TCP connection
# host = 'www.ietf.org'
# port = 80

# sock = socket.create_connection((host, port))

# # implement a full HTTP Get request


# req = (
#        'GET /rfc/rfc{rfcnum}.txt HTTP/1.1\r\n'
#        'Host: {host}:{port}\r\n'
#        'User-Agent: Python {version}\r\n'
#        'Connection: close\r\n'
#        '\r\n'
#    )

# req = req.format(
#        rfcnum=rfc_number,
#        host=host,
#        port=port,
#        version=sys.version_info[0]
#    )


# # the data sent througg TCP must be in raw bytes so we have to encode the request text as ASCII before sending it

# sock.sendall(req.encode('ascii'))
# rfc_raw = bytearray()

# # read the server response
# while True:
# 	# recv function call will return an empty string after server send all its data and closes the connection
# 	buf = sock.recv(4096)
# 	if not len(buf):
# 		break
# 	rfc_raw += buf
	


# rfc = rfc_raw.decode('utf-8')
# print(rfc)
