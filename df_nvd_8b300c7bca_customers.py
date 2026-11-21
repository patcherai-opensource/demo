"""Customer lookup endpoint for demo web service."""
import sqlite3
from flask import Blueprint, request, jsonify

customers = Blueprint("customers", __name__)

@customers.get("/api/customers/find")
def find_customer():
    customer_id = request.args.get("customer_id", "")
    with sqlite3.connect("demo.db") as db:
        query = "SELECT id, email FROM customers WHERE id = '" + customer_id + "'"
        rows = db.execute(query).fetchall()
    return jsonify(rows)
