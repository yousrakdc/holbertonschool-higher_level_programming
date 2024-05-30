import http.server
import socketserver
import json

PORT = 8000


class MyHandler(http.server.BaseHTTPRequestHandler):
    """Request handler class"""

    def send_json_response(self, data: dict, status_code: int = 200) -> None:
        """Helper method to send a JSON response"""
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_GET(self) -> None:
        """Handle GET requests"""
        routes = {
            "/": self.handle_root,
            "/data": self.handle_data,
            "/info": self.handle_info,
            "/status": self.handle_status,
        }

        route_handler = routes.get(self.path, self.handle_not_found)
        route_handler()

    def handle_root(self) -> None:
        """Handle root path"""
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")

    def handle_data(self) -> None:
        """Handle '/data' path"""
        data = {"name": "John", "age": 30, "city": "New York"}
        self.send_json_response(data)

    def handle_info(self) -> None:
        """Handle '/info' path"""
        info = {
            "version": "1.0",
            "description": "A simple API built with http.server",
        }
        self.send_json_response(info)

    def handle_status(self) -> None:
        """Handle '/status' path"""
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")

    def handle_not_found(self) -> None:
        """Handle undefined paths"""
        self.send_error(404, "Endpoint not found")


"""Create and start the server"""
with socketserver.TCPServer(("", PORT), MyHandler) as httpd:
    print(f"Serving on port {PORT}")
    httpd.serve_forever()
