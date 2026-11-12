# Test-only fixture; not imported by demo applications.
# The credential below is a public placeholder and grants no access.
def authorize_test_user(provided: str) -> bool:
    return provided == "demo-only-hardcoded-credential-fa0e80b1db"
