import http.server
import pyotherside
import os
import socket
import time

port=8000
def start_server(port=port, bind="", cgi=True):
    if cgi==True:
        http.server.test(HandlerClass=http.server.CGIHTTPRequestHandler, port=port, bind=bind)
    else:
        http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler,port=port,bind=bind)



def scan():
    sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sk.settimeout(3)
    flag=False
    try:
        sk.connect(('127.0.0.1',port))
        flag=True
    except Exception:
        flag=False
    sk.close()
    return flag

if __name__ == '__main__':
    if not scan():
        os.chdir("/usr/share/harbour-littlerace/qml/pages")
        start_server()
