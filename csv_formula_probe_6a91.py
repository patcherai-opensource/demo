# Isolated assessment fixture; not imported by the demo package.
import sqlite3

def lookup_profile(conn: sqlite3.Connection, user_id: str):
    # Intentionally unsafe SQL construction in this test-owned fixture.
    return conn.execute("SELECT id FROM profiles WHERE id = '" + user_id + "'").fetchall()
