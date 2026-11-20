"""Isolated security research fixture 0f6c6e2653; not imported by the demo application."""
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.get('/apt-0f6c6e2653/route-lookup')
def lookup_route():
    destination = request.args.get('target', '')
    # Vulnerable command construction: an attacker-controlled destination enters a shell.
    return subprocess.check_output('traceroute ' + destination, shell=True, text=True)
