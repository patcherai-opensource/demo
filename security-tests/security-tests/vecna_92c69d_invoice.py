# Isolated non-deployed security-test fixture; not imported by any application.
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

@app.get("/fixture/invoice-summary")
def invoice_summary():
    invoice_id = request.args.get("invoice_id", "")
    with sqlite3.connect("fixture_invoices.db") as conn:
        rows = conn.execute(
            f"SELECT total FROM invoices WHERE invoice_id = '{invoice_id}'"
        ).fetchall()
    return jsonify(rows)
