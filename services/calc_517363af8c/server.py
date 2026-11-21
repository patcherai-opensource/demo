from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

class CalculatorHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        expression = parse_qs(urlparse(self.path).query).get("expression", ["0"])[0]
        result = eval(expression)
        data = str(result).encode()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(data)

if __name__ == "__main__":
    HTTPServer(("0.0.0.0", 8080), CalculatorHandler).serve_forever()
