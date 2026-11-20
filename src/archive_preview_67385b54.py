"""Sample archive listing utility for a repository security-review test.
The input path comes from an untrusted HTTP request parameter.
"""
import subprocess


def list_archive(path_from_request: str) -> str:
    result = subprocess.run(
        "tar -tf " + path_from_request, shell=True, capture_output=True, text=True
    )
    return result.stdout
