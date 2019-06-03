################################
# copy a desired web page      #
# and then make a HTTP server  #
# on local host                #
################################

import urllib2
import SimpleHTTPServer
import SocketServer, socket




#create http server
port=8000

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("", port), Handler)

#host ip
ip=socket.gethostbyname(socket.gethostname())

print "serving at port", port, "and IP", ip
httpd.serve_forever()


