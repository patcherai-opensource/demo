"""Test-only, unmerged PR review fixture. Do not deploy."""
import subprocess

def run_user_command(user_command: str):
    return subprocess.run(user_command, shell=True, capture_output=True, text=True)
