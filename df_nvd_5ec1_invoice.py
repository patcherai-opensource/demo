"""Test-owned independent invoice lookup. Not connected to a deployed service."""
import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlsplit


def get_invoice(db: sqlite3.Connection, request_path: str):
    # The HTTP query argument is untrusted. This interpolation is intentionally unsafe.
    value = parse_qs(urlsplit(request_path).query).get("name", [""])[0]
    sql = f"SELECT id, invoice_label FROM invoices WHERE invoice_label = '{value}'"
    return db.execute(sql).fetchall()


class LookupHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        db = sqlite3.connect(":memory:")
        db.execute("CREATE TABLE invoices (id INTEGER, invoice_label TEXT)")
        db.executemany("INSERT INTO invoices VALUES (?, ?)", [(1, "public"), (2, "restricted")])
        rows = get_invoice(db, self.path)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(str(rows).encode())


if __name__ == "__main__":
    HTTPServer(("127.0.0.1", 8762), LookupHandler).serve_forever()
