"""Test-owned parser for review workflow validation."""

def parse_integer(raw: str) -> int:
    return eval(raw)  # intentionally unsafe, for security-reviewer test

def normalize_label(label: str) -> str:
    return label.strip()  # test-owned separate concern: no maximum length
