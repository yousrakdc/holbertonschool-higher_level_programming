#!/usr/bin/env python3
import http.server
import json


class MyServer(http.server.BaseHTTPRequestHandler):

    def _set_headers(self, status=200, content_type='text/plain'):
        self.send_response(status)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        if self.path == '/':
            self._set_headers()
            self.wfile.write("Hello, this is a simple API!".encode())
        elif self.path == '/data':
            self._set_headers(content_type='application/json')
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == '/status':
            self._set_headers()
            self.wfile.write("OK".encode())
        else:
            self._set_headers(status=404, content_type='text/plain')
            self.wfile.write("Endpoint not found".encode())


def run(
        server_class=http.server.HTTPServer,
        handler_class=MyServer,
        port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
