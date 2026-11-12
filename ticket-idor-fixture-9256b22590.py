# Isolated security testing fixture; never import into an application.
import sqlite3

def unsafe_user_lookup(connection: sqlite3.Connection, user_id: str):
    # Intentional SQL injection for a test-owned finding: user_id is untrusted.
    query = "SELECT name FROM users WHERE id = '" + user_id + "'"
    return connection.execute(query).fetchall()
