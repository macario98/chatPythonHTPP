from http.server import HTTPServer
from server import server
host = '0.0.0.0'
port = 8000
HTTPServer((host, port), server.ServerAPI).serve_forever()