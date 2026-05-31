"""
Secret model.
Represents encrypted secrets.
"""
from datetime import datetime, timezone


class Secret:
    """
     Secret object.
     """
    def __init__(self, secret_id, title, encrypted_value, user_id):
        self.id = secret_id
        self.title = title
        self.encrypted_value = encrypted_value
        self.user_id = user_id
        self.created_at = datetime.now(timezone.utc).isoformat()


    def to_dict(self):
        """
         Convert object to dictionary.
         """
        return {
        "id": self.id,
        "title": self.title,
        "encrypted_value": self.encrypted_value,
        "user_id": self.user_id,
        "created_at": self.created_at
        }