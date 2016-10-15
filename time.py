#!/usr/bin/python
import SimpleHTTPServer
import SocketServer
import time

PORT = 80


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
