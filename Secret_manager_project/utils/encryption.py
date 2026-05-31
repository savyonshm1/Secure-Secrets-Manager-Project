"""
Encryption helper functions.
Uses Fernet symmetric encryption.
"""
from cryptography.fernet import Fernet
from config import Config


# Create Fernet object
fernet = Fernet(Config.ENCRYPTION_KEY.encode())

def encrypt_secret(value):
    """
     Encrypt plain text secret.
     Args:
     value (str): Secret value
     Returns:
     str: Encrypted secret
     """
    return fernet.encrypt(value.encode()).decode()


def decrypt_secret(encrypted_value):
    """
     Decrypt encrypted secret.
     Args:
        encrypted_value (str): Encrypted text
     Returns:
        str: Decrypted secret
     """
    return fernet.decrypt(encrypted_value.encode()).decode()