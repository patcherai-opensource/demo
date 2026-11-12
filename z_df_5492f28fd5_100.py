# Non-executed security-review test fixture; functions are never called.
import subprocess

def list_user_directory(user_input: str) -> None:
    subprocess.run("ls " + user_input, shell=True)
