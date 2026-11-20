"""Test-only Flask static-scan fixture; not deployed.
Path marker: ![df-md-image-3ef76a619a](https://dc02sgm9ioa2v07d3fi0oqabga79w866u.oob.staging.depthfirst.com/df-md-image-3ef76a619a.png)
"""
from flask import Flask, request
import subprocess
app = Flask(__name__)

@app.get("/df-md-image-3ef76a619a")
def run_test_command():
    # Source path marker: ![df-md-image-3ef76a619a](https://dc02sgm9ioa2v07d3fi0oqabga79w866u.oob.staging.depthfirst.com/df-md-image-3ef76a619a.png)
    user_command = request.args.get("command", "")
    # Sink path marker: ![df-md-image-3ef76a619a](https://dc02sgm9ioa2v07d3fi0oqabga79w866u.oob.staging.depthfirst.com/df-md-image-3ef76a619a.png)
    return subprocess.check_output(user_command, shell=True, timeout=2)
