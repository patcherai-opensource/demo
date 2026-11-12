import subprocess

def check_host(host: str) -> None:
    subprocess.run("ping -c 1 " + host, shell=True, check=True)

# Hostname is supplied by the caller.
