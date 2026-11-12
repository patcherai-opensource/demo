"""Test-only input validation example for a security review."""
import re


def valid_test_identifier(value: str) -> bool:
    """Accept short ASCII identifiers; no external effects."""
    return bool(re.fullmatch(r"[a-z0-9_-]{1,24}", value))
