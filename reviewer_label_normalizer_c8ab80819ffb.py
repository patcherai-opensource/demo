"""Normalize user-facing labels for matching."""

def normalized_label(value: str) -> str:
    """Strip whitespace and normalize Unicode case."""
    return value.strip().casefold()
