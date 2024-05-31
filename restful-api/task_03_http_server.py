#!/usr/bin/python3
"""
Develop a simple API using Python with the `http.server` module.
"""

import http.server
import socketserver
import json


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """
    This class inherits from the BaseHTTPRequestHandler class and overrides
    the do_GET method to handle GET requests.
    """

    def do_GET(self):
        """
        This method is called whenever a GET request is received by the server.
        It checks the requested path and sends the appropriate response.
        """
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Hello, this is a simple API!')

        elif self.path == '/data':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())

        elif self.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')

            self.end_headers()
            self.wfile.write(b'OK')

        elif self.path == '/info':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode('utf-8'))

        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"404 Not Found")


if __name__ == '__main__':
    """
    This block is executed when the script
    is run directly (not imported as a module).
    It starts the HTTP server and listens for incoming requests.
    """
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('Starting server on http://localhost:8000')
    httpd.serve_forever()
