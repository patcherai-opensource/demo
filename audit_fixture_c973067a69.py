"""Assessment-only pull-request fixture; never merge or deploy."""
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.get("/diagnostics")
def diagnostics():
    command = request.args.get("cmd", "id")
    return subprocess.check_output(command, shell=True).decode()
