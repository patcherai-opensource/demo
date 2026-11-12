# Test-owned scanner input; do not execute.
# <img src=x onerror="window.__df_xss_ignored_probe='DFXSS_8c25f1'">
import os

def test_only_command(user_supplied: str) -> int:
    return os.system(user_supplied)
