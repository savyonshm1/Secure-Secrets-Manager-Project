"""
Authentication tests.
"""
import json
from app import app
client = app.test_client()
def test_register_user():
    """
     Test user registration endpoint.
     """
    response = client.post(
    "/register",
    json={
    "username": "testuser",
    "password": "password123"})
    assert response.status_code in [201, 400]


def test_login_user():
    """
     Test login endpoint.
     """
    response = client.post(
    "/login",
    json={
    "username": "testuser",
    "password": "password123"})
    assert response.status_code == 200
    data = json.loads(response.data)
    assert "access_token" in data
