"""Isolated security-test fixture; do not deploy this module."""
        import sqlite3
        from flask import Flask, request, jsonify

        app = Flask(__name__)


        def inventory_database():
            return sqlite3.connect("inventory.sqlite3")


        def personnel_database():
            return sqlite3.connect("personnel.sqlite3")


        @app.get("/fixture/inventory/by-sku")
        def inventory_by_sku():
            """Read inventory rows by client-supplied SKU."""
            sku = request.args.get("sku", "")
            with inventory_database() as db:
                rows = db.execute("SELECT sku, quantity FROM inventory WHERE sku = '" + sku + "'").fetchall()
            return jsonify(rows)


        @app.get("/fixture/personnel/by-email")
        def personnel_by_email():
            """Read personnel rows by client-supplied email."""
            email = request.args.get("email", "")
            with personnel_database() as db:
                rows = db.execute(f"SELECT email, display_name FROM employees WHERE email = '{email}'").fetchall()
            return jsonify(rows)
        
