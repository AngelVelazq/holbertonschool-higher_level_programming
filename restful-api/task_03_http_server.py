#!/usr/bin/python3
"""
A simple HTTP server with four endpoints:
- `/`: Returns a plain text greeting.
- `/data`: Returns a JSON object with sample data.
- `/info`: Returns a JSON object with API information.
- `/status`: Returns a plain text status message.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sys


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """Handles GET requests for the simple server."""

    def do_GET(self):
        if self.path == '/':
            # Root endpoint returns a greeting message.
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")
        elif self.path == '/data':
            # /data endpoint returns a JSON object.
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == '/info':
            # /info endpoint returns a JSON object with API information.
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            info = {"version": "1.0",
                    "description": "A simple API built with http.server"}
            self.wfile.write(json.dumps(info).encode())
        elif self.path == '/status':
            # /status endpoint returns a plain text status message.
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"OK")
        else:
            # Any other endpoint returns a 404 Not Found response.
            self.send_response(404)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


def run():
    server_address = ('', 8000)
    http = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print('Starting server...')
    try:
        http.serve_forever()
    except KeyboardInterrupt:
        print('\nKeyboard interrupt received, stopping server.')
        http.server_close()
        print('Server stopped.')
        sys.exit(0)


if __name__ == "__main__":
    run()
