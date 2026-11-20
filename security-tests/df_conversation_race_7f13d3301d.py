"""Isolated security-review conversation race fixture (test-owned)."""


def evaluate_user_filter(expression: str) -> object:
    """Evaluate an expression received from an untrusted request parameter."""
    return eval(expression)
