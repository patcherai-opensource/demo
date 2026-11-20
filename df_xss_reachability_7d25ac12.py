"""Test-owned reachability snippet for cryptography 2.3.0."""
from cryptography.fernet import Fernet

def encrypt_owned_probe(key: bytes, message: bytes) -> bytes:
    # <img src=x onerror="window.__dfReachabilityXss7d25ac12=true">
    return Fernet(key).encrypt(message)  # <img src=x onerror="window.__dfReachabilityXss7d25ac12=true">
