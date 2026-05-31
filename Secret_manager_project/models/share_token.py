"""
Share token model.
Used for one-time secret sharing.
"""
from datetime import datetime, timedelta, timezone


class ShareToken:
    """
     ShareToken object.
     """
    def __init__(self, token, secret_id):
        self.token = token
        self.secret_id = secret_id
        self.used = False

        # Token expires after 1 hour
        self.expires_at = (datetime.now(timezone.utc) + timedelta(hours=1)).isoformat()


    def to_dict(self):
        """
         Convert object to dictionary.
         """
        return {
        "token": self.token,
        "secret_id": self.secret_id,
        "used": self.used,
        "expires_at": self.expires_at
        }