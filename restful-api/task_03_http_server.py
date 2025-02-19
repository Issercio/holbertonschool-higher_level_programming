#!/usr/bin/python3
'''model of http_server
'''


import json
from http.server import BaseHTTPRequestHandler, HTTPServer


# Définition du handler pour gérer les requêtes HTTP
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        """Gère les requêtes GET envoyées au serveur."""

        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "OK"}).encode("utf-8"))

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            error_message = {"error": "Endpoint not found"}
            self.wfile.write(json.dumps(error_message).encode("utf-8"))


# Démarrage du serveur
def run(
    server_class=HTTPServer,
    handler_class=SimpleHTTPRequestHandler,
    port=8000
):
    server_address = ("", port)  # Écoute sur toutes les interfaces
    httpd = server_class(server_address, handler_class)
    print(
        "Server running on http://localhost:",
        port
    )  # Print split into two parts to avoid exceeding 79 characters
    httpd.serve_forever()


if __name__ == "__main__":
    run()
