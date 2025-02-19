#!/usr/bin/python3
'''model of http_server
'''


import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """Custom HTTP request handler for a simple API."""

    def do_GET(self):
        """Handle GET requests and serve appropriate responses."""
        if self.path == "/":
            self.send_plain_text_response(200, "Hello, this is a simple API!")

        elif self.path == "/data":
            data = {"name": "John", "age": 30, "city": "New York"}
            self.send_json_response(200, data)

        elif self.path == "/status":
            self.send_plain_text_response(200, "OK")

        elif self.path == "/info":
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self.send_json_response(200, info)

        else:
            error_message = {"error": "Endpoint not found"}
            self.send_json_response(404, error_message)

    def send_plain_text_response(self, status_code, message):
        """Send a plain text response."""
        self.send_response(status_code)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

    def send_json_response(self, status_code, data):
        """Send a JSON response."""
        self.send_response(status_code)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    """Start the HTTP server on the specified port."""
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()


if __name__ == "__main__":
    run()
