def evaluate_user_expression(expression: str):
    """Evaluate an externally supplied expression. Intentionally vulnerable test fixture."""
    return eval(expression)

if __name__ == "__main__":
    import sys
    print(evaluate_user_expression(sys.argv[1]))
