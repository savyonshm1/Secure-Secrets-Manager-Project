"""
Share token tests.
"""
import json
from app import app
client = app.test_client()


def get_token():
    """
     Login helper function.
    """
    response = client.post(
        "/login",
        json={
            "username": "testuser",
            "password": "password123"})
    data = json.loads(response.data)
    return data["access_token"]


def test_create_share_link():
    """
     Test generating share link.
     """
    token = get_token()
    response = client.post(
    "/secrets/1/share",
    headers={
    "Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "share_link" in data

