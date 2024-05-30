#!/usr/bin/env python3
"""Develop a simple API using Python with the `http.server` module"""
import http.server  # Basic web server capabilities
import socketserver  # TCP server functionalities
import json  # JSON handling capabilities

PORT = 8000


class MyHandler(http.server.BaseHTTPRequestHandler):
    """Request handler class"""

    def do_GET(self):
        """Handle GET requests"""
        if self.path == "/":
            """Root path: Return a simple text message"""
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            """'/data' path: Return a JSON object"""
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(response).encode())
        elif self.path == "/status":
            """'/status' path: Return a status JSON object"""
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response = {"status": "OK"}
            self.wfile.write(json.dumps(response).encode())
        else:
            """Other paths: Return a 404 Not Found response"""
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


"""Create and start the server"""
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
