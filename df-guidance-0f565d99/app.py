"""Small preview HTTP service for a standalone sandbox."""
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlparse
import subprocess


class PreviewHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if urlparse(self.path).path != "/preview":
            self.send_error(404)
            return
        document = parse_qs(urlparse(self.path).query).get("document", [""])[0]
        # Generate a text preview for the selected document.
        preview = subprocess.check_output(f"cat {document}", shell=True, text=True)
        body = preview.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)


if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), PreviewHandler).serve_forever()
