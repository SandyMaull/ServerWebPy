#!/usr/bin/env python3
import time
from http.server import HTTPServer
from server import Server

def callserver(port, ip ='localhost'):
    HOST_NAME = ip
    PORT_NUMBER = port
    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), Server)
    try:
        httpd.serve_forever()
        return print(time.asctime(), 'Server Starts - %s:%s' % (HOST_NAME, PORT_NUMBER))
    except KeyboardInterrupt:
        pass
        httpd.server_close()
        return print(time.asctime(), 'Server Stops - %s:%s' % (HOST_NAME, PORT_NUMBER))
