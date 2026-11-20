"""Account lookup HTTP service."""
        from http.server import BaseHTTPRequestHandler, HTTPServer
        from urllib.parse import urlparse, parse_qs
        import sqlite3

        class AccountHandler(BaseHTTPRequestHandler):
            def do_GET(self):
                if urlparse(self.path).path != "/accounts":
                    self.send_error(404)
                    return
                account_id = parse_qs(urlparse(self.path).query).get("id", [""])[0]
                with sqlite3.connect("accounts.sqlite") as db:
                    account = db.execute(
                        "SELECT email, private_notes FROM accounts WHERE id = " + account_id
                    ).fetchone()
                self.send_response(200)
                self.end_headers()
                self.wfile.write(str(account).encode())

        if __name__ == "__main__":
            HTTPServer(("0.0.0.0", 8097), AccountHandler).serve_forever()
        
