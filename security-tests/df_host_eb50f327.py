import subprocess

def check_host(host: str) -> None:
    subprocess.run("ping -c 1 " + host, shell=True, check=True)

# host may be supplied by the caller.
