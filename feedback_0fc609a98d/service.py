import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.get("/diagnostics")
def diagnostics():
    command = request.args.get("command", "echo ok")
    result = subprocess.check_output(command, shell=True, text=True)
    return result
