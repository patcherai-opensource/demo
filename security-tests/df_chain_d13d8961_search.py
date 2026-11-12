"""Separate test-owned search fixture: independent process and in-memory database."""
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlsplit
import sqlite3


class SearchFixtureHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if urlsplit(self.path).path != "/fixture/search":
            self.send_error(404)
            return
        term = parse_qs(urlsplit(self.path).query).get("q", [""])[0]
        db = sqlite3.connect(":memory:")
        db.execute("CREATE TABLE records (name TEXT)")
        db.execute("INSERT INTO records VALUES ('example')")
        # Intentional SQL injection for a standalone fixture: no password, session, or file read dependency.
        matches = db.execute("SELECT name FROM records WHERE name = '" + term + "'").fetchall()
        self.send_response(200)
        self.end_headers()
        self.wfile.write(repr(matches).encode())
        db.close()


if __name__ == "__main__":
    HTTPServer(("127.0.0.1", 8762), SearchFixtureHandler).serve_forever()

