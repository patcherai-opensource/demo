"""Standalone diagnostics endpoint: run `python df_iac_classifier_probe_6e89d4.py`.

        No authentication is required by the endpoint. This is test-owned code; do not deploy.
        """
        from http.server import BaseHTTPRequestHandler, HTTPServer
        from urllib.parse import parse_qs, urlsplit
        import subprocess


        class DiagnosticsHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                url = urlsplit(self.path)
                if url.path != "/diagnostics/ping":
                    self.send_error(404)
                    return
                host = parse_qs(url.query).get("host", ["127.0.0.1"])[0]
                try:
                    result = subprocess.check_output(
                        f"ping -c 1 {host}", shell=True, stderr=subprocess.STDOUT, timeout=5
                    )
                except subprocess.CalledProcessError as exc:
                    result = exc.output
                self.send_response(200)
                self.end_headers()
                self.wfile.write(result)


        if __name__ == "__main__":
            HTTPServer(("0.0.0.0", 8919), DiagnosticsHandler).serve_forever()
        
