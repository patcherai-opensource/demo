# Isolated non-deployed security-test fixture; not imported by any application.
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

@app.get("/fixture/customer-summary")
def customer_summary():
    customer_id = request.args.get("customer_id", "")
    with sqlite3.connect("fixture_customers.db") as conn:
        rows = conn.execute(
            f"SELECT email FROM customers WHERE customer_id = '{customer_id}'"
        ).fetchall()
    return jsonify(rows)
