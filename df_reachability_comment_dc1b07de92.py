from cryptography.hazmat.primitives.asymmetric import padding


def decrypt_rsa_pkcs1_v15(private_key, ciphertext):
    """Return the RSA PKCS#1 v1.5 plaintext for supplied test inputs."""
    return private_key.decrypt(ciphertext, padding.PKCS1v15())
