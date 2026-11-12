"""Isolated test fixture for API review baseline comparison; do not deploy."""
import subprocess

def run_authorized_command(user_supplied_command: str):
    return subprocess.run(user_supplied_command, shell=True, capture_output=True)
