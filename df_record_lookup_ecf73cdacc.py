import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/account")
def account():
    account_id = request.args.get("id", "")
    db = sqlite3.connect("accounts.db")
    record = db.execute("SELECT email, private_notes FROM accounts WHERE id = '" + account_id + "'").fetchone()
    return jsonify({"email": record[0], "private_notes": record[1]}) if record else ("Not found", 404)
