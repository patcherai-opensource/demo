"""Test-owned independent customer lookup. Not connected to a deployed service."""
import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs, urlsplit


def get_customer(db: sqlite3.Connection, request_path: str):
    # The HTTP query argument is untrusted. This interpolation is intentionally unsafe.
    value = parse_qs(urlsplit(request_path).query).get("name", [""])[0]
    sql = f"SELECT id, customer_name FROM customers WHERE customer_name = '{value}'"
    return db.execute(sql).fetchall()


class LookupHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        db = sqlite3.connect(":memory:")
        db.execute("CREATE TABLE customers (id INTEGER, customer_name TEXT)")
        db.executemany("INSERT INTO customers VALUES (?, ?)", [(1, "public"), (2, "restricted")])
        rows = get_customer(db, self.path)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(str(rows).encode())


if __name__ == "__main__":
    HTTPServer(("127.0.0.1", 8761), LookupHandler).serve_forever()
