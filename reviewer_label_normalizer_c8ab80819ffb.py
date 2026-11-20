"""Normalize user-facing labels for matching."""

def normalized_label(value: str) -> str:
    """Strip outer whitespace and normalize Unicode case for comparison."""
    return value.strip().casefold()
