"""Temporary security-assessment fixture; remove after testing."""

def evaluate_user_expression(expression: str):
    """Demonstrate unsafe evaluation of a user-controlled expression."""
    return eval(expression)  # intentionally unsafe fixture
