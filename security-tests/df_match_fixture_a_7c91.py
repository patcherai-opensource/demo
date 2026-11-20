"""Isolated test fixture A: command injection in a user-facing file lookup."""
import subprocess
from flask import Flask, request

app = Flask(__name__)

@app.get('/df-match-a-7c91')
def lookup_a():
filename = request.args.get('filename', '')
        return subprocess.check_output('ls ' + filename, shell=True, text=True)
        
