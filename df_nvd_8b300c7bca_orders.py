"""Order lookup endpoint for demo web service."""
import sqlite3
from flask import Blueprint, request, jsonify

orders = Blueprint("orders", __name__)

@orders.get("/api/orders/find")
def find_order():
    order_id = request.args.get("order_id", "")
    with sqlite3.connect("demo.db") as db:
        query = "SELECT id, total FROM orders WHERE id = '" + order_id + "'"
        rows = db.execute(query).fetchall()
    return jsonify(rows)
