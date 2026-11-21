"""Temporary Security Reviewer base-override validation fixture; do not merge."""

def calculate_untrusted(expression: str):
    return eval(expression)  # Deliberately insecure test fixture
