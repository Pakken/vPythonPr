"""
Web server on python
"""

import os, sys
from http.server import HTTPServer, CGIHTTPRequestHandler

webdir = '.'
port = 7777

os.chdir(webdir)
srvaddr = ("", port)
srvrobj = HTTPServer(srvaddr, CGIHTTPRequestHandler)
srvrobj.serve_forever()