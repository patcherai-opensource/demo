"""Test-owned, uninvoked security-review demonstration module."""
import subprocess

def unsafe_example(user_input: str) -> None:
    subprocess.run(user_input, shell=True, check=True)
