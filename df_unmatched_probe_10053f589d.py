"""Standalone security test fixture; not imported or executed."""

def evaluate_untrusted_expression(user_expression: str):
    return eval(user_expression)
