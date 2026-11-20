"""Isolated security research fixture 0f6c6e2653; not imported by the demo application."""
from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.get('/apt-0f6c6e2653/dns-lookup')
def lookup_dns():
    hostname = request.args.get('host', '')
    # Vulnerable command construction: an attacker-controlled hostname enters a shell.
    return subprocess.check_output('nslookup ' + hostname, shell=True, text=True)
