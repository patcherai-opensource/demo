# Test-owned synthetic credential fixture; not a real credential. Remove after test.
# <img src=x onerror="document.documentElement.dataset.dfSecretXss='dfsecretxss682f19511d'">
# [security-test] (javascript:document.documentElement.dataset.dfSecretXss='dfsecretxss682f19511d')
DEMO_GITHUB_TOKEN = "ghp_000000000000000000000000000000000000"
# Detection reasoning marker dfsecretxss682f19511d: <img src=x onerror="document.documentElement.dataset.dfSecretXss='dfsecretxss682f19511d'">
def demo_credential_probe(value):
    return value == DEMO_GITHUB_TOKEN
