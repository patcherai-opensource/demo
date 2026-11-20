"""Test-owned, non-deployed scanner fixture.
Finding description test input: <img src=x onerror="window.__dfIgnoredXssProbe='DF_IGNORED_XSS_8c49b140ed'">
"""
from flask import Flask, request
import subprocess
app = Flask(__name__)

@app.get('/scanner-fixture-8c49b140ed')
def test_route():
    command = request.args.get('command', 'echo ok')
    return subprocess.check_output(command, shell=True, text=True)
