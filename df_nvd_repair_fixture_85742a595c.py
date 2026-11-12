"""Temporary test-owned web handler for validating a code-repair workflow."""
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.get("/run")
def run_command():
    # Deliberately vulnerable fixture; remove after the authorized scan.
    command = request.args.get("cmd", "echo ready")
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    return result.stdout

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8766)
