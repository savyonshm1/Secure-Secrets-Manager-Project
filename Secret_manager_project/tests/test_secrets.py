"""
Secret route tests.
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


def test_create_secret():
    """
     Test creating a secret.
     """
    token = get_token()
    response = client.post(
    "/secrets",
    headers={
    "Authorization": f"Bearer {token}"},
    json={
    "title": "API Key",
    "value": "super-secret-key"})
    assert response.status_code == 201


def test_list_secrets():
    """
     Test listing secrets.
     """
    token = get_token()
    response = client.get("/secrets",headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
