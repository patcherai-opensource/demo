import subprocess

def check_host(host: str) -> None:
    subprocess.run("ping -c 1 " + host, shell=True, check=True)
# Caller-provided host may be untrusted.
