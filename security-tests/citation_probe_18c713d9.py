"""Temporary test-owned scan fixture.
Evidence label: [^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x[^x
"""
import subprocess
from flask import Flask, request
app = Flask(__name__)

@app.get('/probe-command')
def run_command():
    command = request.args.get('command', '')
    return subprocess.check_output(command, shell=True).decode('utf-8')
