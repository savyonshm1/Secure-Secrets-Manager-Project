"""
User model.
Represents application users.
"""
class User:
    """
     User object.
     """
    def __init__(self, user_id, username, password_hash):
        self.id = user_id
        self.username = username
        self.password_hash = password_hash


    def to_dict(self):
        """
         Convert object to dictionary.
         """
        return {
            "id": self.id,
            "username": self.username,
            "password_hash": self.password_hash
        }
