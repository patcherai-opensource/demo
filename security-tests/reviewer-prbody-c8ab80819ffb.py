"""Small review fixture: bounded normalization of sample labels."""

def normalize_label(value: str) -> str:
    return value.strip().lower()
