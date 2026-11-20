import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.get("/test-only/record")
def get_record():
    record_id = request.args.get("record_id", "")
    conn = sqlite3.connect(":memory:")
    row = conn.execute("SELECT secret FROM records WHERE id = '" + record_id + "'").fetchone()
    return jsonify({"record": row[0] if row else None})
