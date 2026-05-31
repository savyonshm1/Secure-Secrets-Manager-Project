"""
Key generation script.

This script generates secure values for:
- Flask SECRET_KEY
- JWT_SECRET_KEY
- Fernet ENCRYPTION_KEY

It also automatically creates a .env file.
"""

import secrets
from cryptography.fernet import Fernet


def generate_secret_key():
    """
    Generate secure random string.

    Returns:
        str: Secure hex token
    """

    return secrets.token_hex(32)


def generate_encryption_key():
    """
    Generate Fernet encryption key.

    Returns:
        str: Fernet key
    """

    return Fernet.generate_key().decode()


def create_env_file():
    """
    Create .env file with generated keys.
    """

    secret_key = generate_secret_key()

    jwt_secret_key = generate_secret_key()

    encryption_key = generate_encryption_key()

    env_content = f"""
SECRET_KEY={secret_key}
JWT_SECRET_KEY={jwt_secret_key}
ENCRYPTION_KEY={encryption_key}
"""

    # creates the file if it doesn't exist or overrides content if it does exist
    with open(".env", "w") as env_file:
        env_file.write(env_content.strip())

    print("✅ .env file created successfully!")
    print()
    print(env_content)


if __name__ == "__main__":
    create_env_file()