"""Temporary test-owned fixture; do not deploy this demonstration handler."""
import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.get("/df-overlap-test")
def test_command():
    subprocess.run("printf %s " + request.args.get("one", ""), shell=True) if request.args.get("mode") == "one" else None
    return "ok"
