"""
Authentication routes.
"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from models.user import User
from utils.auth import hash_password, verify_password
from utils.file_db import (USERS_FILE, load_data, save_data)
from utils.logger import log_event


auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/register", methods=["POST"])
def register():
    """
     Register new user.
     """
    data = request.get_json()
    users = load_data(USERS_FILE)
    # Check if username already exists
    for user in users:
        if user["username"] == data["username"]:
            return jsonify({"error": "User already exists"}), 400

    # Generate new user ID (if the user doesn't exist)
    # find the max id number and add 1 for the new user id
    if users:
        user_id = max(user["id"] for user in users) + 1
    else:
        user_id = 1
    # Create user object
    user = User(
    user_id=user_id,
    username=data["username"],
    password_hash=hash_password(data["password"])
    )
    users.append(user.to_dict())
    save_data(USERS_FILE, users)
    return jsonify({"message": "User registered"}), 201


@auth_bp.route("/login", methods=["POST"])
def login():
    """
     Authenticate user.
     """
    data = request.get_json()
    users = load_data(USERS_FILE)
    for user in users:
        if user["username"] == data["username"]:
            if verify_password(data["password"],user["password_hash"]):
                token = create_access_token(identity=str(user["id"]))
                # add login log
                log_event(
                    f"User '{user['username']}' logged in"
                )
                return jsonify({"access_token": token})
    # if the user isn't authenticated
    return jsonify({"error": "Invalid credentials"}), 401
