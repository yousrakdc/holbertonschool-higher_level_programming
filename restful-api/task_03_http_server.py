#!/usr/bin/env python3

import http.server
import json

PORT = 8000


class MyHandler(http.server.BaseHTTPRequestHandler):
    """Request handler class"""

    def send_json_response(self, data: dict, status_code: int = 200):
        """Helper method to send a JSON response"""
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self):
        """Handle GET requests"""
        routes = {
            "/": self.handle_root,
            "/data": self.handle_data,
            "/info": self.handle_info,
            "/status": self.handle_status,
        }

        route_handler = routes.get(self.path, self.handle_not_found)
        route_handler()

    def handle_root(self):
        """Handle root path"""
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")

    def handle_data(self):
        """Handle '/data' path"""
        data = {"name": "John", "age": 30, "city": "New York"}
        self.send_json_response(data)

    def handle_info(self):
        """Handle '/info' path"""
        info = {
            "version": "1.0",
            "description": "A simple API built with http.server",
        }
        self.send_json_response(info)

    def handle_status(self):
        """Handle '/status' path"""
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")

    def handle_not_found(self):
        """Handle undefined paths"""
        self.send_error(404, "Endpoint not found")


"""Create and start the server"""
if __name__ == '__main__':
    server_address = ('', 8000)
    httpd = http.server.HTTPServer(server_address, MyHandler)
    print('Starting server on http://localhost:8000')
    httpd.serve_forever()
