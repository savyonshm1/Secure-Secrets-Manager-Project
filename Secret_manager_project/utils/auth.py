"""
Authentication helper functions.
"""
import bcrypt


def hash_password(password):
    """
     Hash user password using bcrypt.
     Args:
     password (str): Plain text password
     Returns:
     str: Hashed password
     """
    return bcrypt.hashpw(password.encode(),
    bcrypt.gensalt()).decode()


def verify_password(password, hashed_password):
    """
     Verify password against stored hash.
     Args:
     password (str): User password
     hashed_password (str): Stored password hash
     Returns:
     bool: True if password matches
     """
    return bcrypt.checkpw(password.encode(),
    hashed_password.encode())