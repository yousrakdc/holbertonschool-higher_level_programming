#!/usr/bin/env python3
"""Develop a simple API using Python with the `http.server` module"""
import http.server  # Basic web server capabilities
import socketserver  # TCP server functionalities
import json  # JSON handling capabilities
import logging

PORT = 8000


class MyHandler(http.server.BaseHTTPRequestHandler):
    """Request handler class"""

    def do_GET(self):
        """Handle GET requests"""
        if self.path == "/":
            """Root path: Return a simple text message"""
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_header()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == "/data":
            """'/data' path: Return a JSON object"""
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_header()
            response = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(response).encode())
        elif self.path == "/status":
            """'/status' path: Return a status JSON object"""
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_header()
            response = {"status": "OK"}
            self.wfile.write(json.dumps(response).encode())
        else:
            """Other paths: Return a 404 Not Found response"""
            self.send_error(404, "Endpoint not found")
            logging.warning(f"Requested path: {self.path}")


"""Create and start the server"""
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    logging.info(f"Serving on port {PORT}")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        logging.info("Server stopped by user")
    finally:
        httpd.server_close()
