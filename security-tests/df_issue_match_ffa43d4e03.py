import subprocess
from urllib.parse import parse_qs

def unsafe_preview_handler(request_query):
    values = parse_qs(request_query)
    command = values.get("command", ["echo fixture"])[0]
    return subprocess.check_output(command, shell=True, text=True)
