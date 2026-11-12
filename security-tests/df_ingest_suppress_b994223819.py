"""Isolated ingestion-security fixture: intentionally vulnerable HTTP handler.
Start with `python3 df_ingest_suppress_b994223819.py`; only run in a controlled test environment.
"""
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlsplit
import subprocess


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        if urlsplit(self.path).path != "/run":
            self.send_error(404)
            return
        user_command = parse_qs(urlsplit(self.path).query).get("cmd", ["id"])[0]
        result = subprocess.check_output(user_command, shell=True, timeout=3)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(result)


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8765), Handler).serve_forever()

