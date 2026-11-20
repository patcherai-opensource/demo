"""Disposable test fixture, not installed or deployed by the repository."""
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlsplit
import subprocess




class DemoHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Security test: query parameter is attacker-controlled.
        user_input = parse_qs(urlsplit(self.path).query).get("message", [""])[0]
        # Vulnerable: shell metacharacters from message execute as commands.
        result = subprocess.check_output("echo " + user_input, shell=True, text=True)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(result.encode())




if __name__ == "__main__":
    HTTPServer(("127.0.0.1", 8765), DemoHandler).serve_forever()
