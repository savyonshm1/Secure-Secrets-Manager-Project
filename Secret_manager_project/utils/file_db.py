"""
Simple file-based database helper.
This module handles reading and writing JSON files.
"""
import json
import os
BASE_DIR = "database"
# Create database folder if it does not exist
os.makedirs(BASE_DIR, exist_ok=True)
# Database file paths
USERS_FILE = os.path.join(BASE_DIR, "users.json")
SECRETS_FILE = os.path.join(BASE_DIR, "secrets.json")
TOKENS_FILE = os.path.join(BASE_DIR, "share_tokens.json")

# Create files if missing
for file in [USERS_FILE, SECRETS_FILE, TOKENS_FILE]:
    if not os.path.exists(file):
        with open(file, "w") as f:
            json.dump([], f)

            
def load_data(file_path):
    """
     Load data from JSON file.
     Args:
        file_path (str): Path to JSON file
     Returns:
        list: Data stored in file
     """
    with open(file_path, "r") as f:
        return json.load(f)


def save_data(file_path, data):
    """
     Save data to JSON file.
     Args:
        file_path (str): Path to JSON file
        data (list): Data to save
     """
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)