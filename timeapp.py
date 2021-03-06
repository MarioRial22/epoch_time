#!/usr/bin/python
import SimpleHTTPServer
import SocketServer
import time
import os

PORT = 80

if os.environ['PORT']:
    PORT = int(os.environ['PORT'])

class CustomHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(str(int(time.time())))


httpd = SocketServer.TCPServer(("", PORT), CustomHandler)


    
print "serving at port", PORT
httpd.serve_forever()
