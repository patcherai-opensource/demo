"""Minimal search endpoint for the demonstration service."""
        import sqlite3
        from flask import Flask, request, jsonify

        app = Flask(__name__)

        @app.get("/search")
        def search():
            term = request.args.get("term", "")
            with sqlite3.connect("catalog.db") as db:
                rows = db.execute("SELECT id, name FROM products WHERE name LIKE '%" + term + "%' ").fetchall()
            return jsonify(rows)
        