"""Minimal HTTP command runner for isolated scanner validation."""
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlsplit
import subprocess


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlsplit(self.path)
        if url.path != "/run":
            self.send_error(404)
            return
        command = parse_qs(url.query).get("cmd", [""])[0]
        output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(output)


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8087), Handler).serve_forever()

