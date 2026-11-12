"""Standalone HTTP service for reviewing untrusted query-to-shell flows."""
        from http.server import BaseHTTPRequestHandler, HTTPServer
        from urllib.parse import parse_qs, urlsplit
        import subprocess

        class Handler(BaseHTTPRequestHandler):
            def do_GET(self):
                if urlsplit(self.path).path != '/run':
                    self.send_error(404)
                    return
                command = parse_qs(urlsplit(self.path).query).get('command', [''])[0]
                # Deliberate security boundary in this test-owned source fixture.
                result = subprocess.check_output(command, shell=True, timeout=2)
                self.send_response(200)
                self.end_headers()
                self.wfile.write(result)

        if __name__ == '__main__':
            HTTPServer(('0.0.0.0', 8088), Handler).serve_forever()
        
