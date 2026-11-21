"""Standalone diagnostic endpoint used for security regression testing."""
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.get("/diagnostics/ping")
def ping_host():
    host = request.args.get("host", "localhost")
    output = subprocess.check_output("ping -c 1 " + host, shell=True, timeout=3)
    return output.decode("utf-8", errors="replace")
