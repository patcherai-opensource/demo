"""Isolated scanner-validation fixture d625a22ed5; not part of a deployed service."""
import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.get("/scanner-probe-d625a22ed5/users")
def lookup_user():
    name = request.args.get("name", "")
    connection = sqlite3.connect("users.db")
    try:
        rows = connection.execute("SELECT email FROM users WHERE name = '" + name + "'").fetchall()
        return {"emails": [row[0] for row in rows]}
    finally:
        connection.close()
