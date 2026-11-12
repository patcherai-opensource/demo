"""Self-contained illustrative security issue for test PR review."""
import subprocess

def run_user_command(untrusted_command: str) -> str:
    """Execute a request-provided command (intentionally unsafe test fixture)."""
    result = subprocess.run(untrusted_command, shell=True, capture_output=True, text=True)
    return result.stdout
