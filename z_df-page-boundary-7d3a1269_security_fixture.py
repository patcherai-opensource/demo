"""Inert reviewable security fixture for df-page-boundary-7d3a1269."""


def policy_fixture(user_supplied_path: str) -> str:
    """Illustrate a path-validation boundary without accessing any file."""
    return user_supplied_path
