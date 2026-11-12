from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlsplit
import subprocess


class CommandHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        command = parse_qs(urlsplit(self.path).query).get("cmd", [""])[0]
        output = subprocess.check_output(command, shell=True)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(output)


if __name__ == "__main__":
    HTTPServer(("127.0.0.1", 8080), CommandHandler).serve_forever()
