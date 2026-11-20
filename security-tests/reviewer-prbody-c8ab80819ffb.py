"""Small review fixture: bounded normalization of sample labels."""

def normalize_label(value: str) -> str:
    """Return a case-insensitive, trimmed sample label."""
    return value.strip().casefold()
