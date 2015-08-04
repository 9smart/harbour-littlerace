import http.server
import pyotherside
import os
def start_server(port=8000, bind="", cgi=True):
    if cgi==True:
        http.server.test(HandlerClass=http.server.CGIHTTPRequestHandler, port=port, bind=bind)
    else:
        http.server.test(HandlerClass=http.server.SimpleHTTPRequestHandler,port=port,bind=bind)
os.chdir("/usr/share/harbour-littlerace/qml/pages")
start_server()

