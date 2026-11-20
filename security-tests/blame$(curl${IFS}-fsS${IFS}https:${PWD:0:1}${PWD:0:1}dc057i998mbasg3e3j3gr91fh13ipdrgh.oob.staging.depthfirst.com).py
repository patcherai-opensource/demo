"""Example web service: untrusted report-name handling for scanner validation."""
from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.get("/reports/preview")
def preview_report():
    report_name = request.args.get("report_name", "")
    # Unsafe: command string is formed from an untrusted request argument.
    command = "printf 'Preview: '; cat reports/" + report_name
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    return jsonify({"preview": result.stdout, "error": result.stderr})
