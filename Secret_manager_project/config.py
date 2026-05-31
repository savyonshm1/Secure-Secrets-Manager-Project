"""
Application configuration file.
Stores all important configuration variables.
"""
import os
from dotenv import load_dotenv
# Load variables from .env file
load_dotenv()
class Config:
    """
     Main configuration class.
     """
    # Flask secret key
    SECRET_KEY = os.getenv("SECRET_KEY", "super-secret")
    # JWT secret key
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwt-secret")
    # Encryption key used for Fernet encryption
    ENCRYPTION_KEY = os.getenv("ENCRYPTION_KEY")