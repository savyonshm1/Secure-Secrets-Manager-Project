"""
Secret management routes.
"""
from flask import Blueprint, request, jsonify
from flask_jwt_extended import (jwt_required, get_jwt_identity)
from models.secret import Secret
from utils.encryption import (encrypt_secret, decrypt_secret)
from utils.file_db import (SECRETS_FILE, load_data, save_data)
from utils.logger import log_event


secret_bp = Blueprint("secrets", __name__)
@secret_bp.route("/secrets", methods=["POST"])
@jwt_required()
def create_secret():
    """
     Store encrypted secret.
     """
    user_id = int(get_jwt_identity())
    data = request.get_json()
    secrets = load_data(SECRETS_FILE)
    # find the max id number and add 1 for the new secret id
    if secrets:
        secret_id = max(secret["id"] for secret in secrets) + 1
    else:
        secret_id = 1
    secret = Secret(
    secret_id=secret_id,
    title=data["title"],
    encrypted_value=encrypt_secret(data["value"]),
    user_id=user_id
    )
    secrets.append(secret.to_dict())
    save_data(SECRETS_FILE, secrets)
    log_event(
        f"User {user_id} created secret {secret_id}"
    )
    return jsonify({"message": "Secret stored"}), 201


@secret_bp.route("/secrets", methods=["GET"])
@jwt_required()
def list_secrets():
    """
     List all secrets for authenticated user.
     """
    user_id = int(get_jwt_identity())
    secrets = load_data(SECRETS_FILE)
    user_secrets = []
    # Iterate through all secrets
    for secret in secrets:
        # once the user is found by its id
        if secret["user_id"] == user_id:
            user_secrets.append({
                "id": secret["id"],
                "title": secret["title"],
                "created_at": secret["created_at"]})
    # Return all user secrets after loop completes
    return jsonify(user_secrets)


@secret_bp.route("/secrets/<int:secret_id>", methods=["GET"])
@jwt_required()
def get_secret(secret_id):
    """
     Retrieve secret if owner has permission.
     """
    user_id = int(get_jwt_identity())
    secrets = load_data(SECRETS_FILE)
    for secret in secrets:
        # once found the secret by its id
        if secret["id"] == secret_id and secret["user_id"] == user_id:
            return jsonify({
            "title": secret["title"],
            "value": decrypt_secret(
            secret["encrypted_value"]
            )})
    log_event(
        f"User {user_id} accessed secret {secret_id}"
    )
    return jsonify({"error": "Secret not found"}), 404


@secret_bp.route("/secrets/<int:secret_id>", methods=["DELETE"])
@jwt_required()
def delete_secret(secret_id):
    """
     Delete user secret.
     """
    user_id = int(get_jwt_identity())
    secrets = load_data(SECRETS_FILE)
    updated_secrets = []
    deleted = False
    for secret in secrets:
        # search the secret by its id and checks user id
        if secret["id"] == secret_id and secret["user_id"] == user_id:
            deleted = True
            continue
        updated_secrets.append(secret)
    # if the secret was not found
    if not deleted:
        return jsonify({"error": "Secret not found"}), 404
    save_data(SECRETS_FILE, updated_secrets)
    log_event(
        f"User {user_id} deleted secret {secret_id}"
    )
    return jsonify({"message": "Secret deleted"})


@secret_bp.route("/secrets/<int:secret_id>", methods=["PUT"])
@jwt_required()
def update_secret(secret_id):
    """
     Update secret metadata.
     """
    user_id = int(get_jwt_identity())
    data = request.get_json()
    secrets = load_data(SECRETS_FILE)
    for secret in secrets:
        # once found the secret - update data
        if secret["id"] == secret_id and secret["user_id"] == user_id:
            secret["title"] = data.get("title", secret["title"])
            save_data(SECRETS_FILE, secrets)
            log_event(
                f"User {user_id} updated secret {secret_id}"
            )
            return jsonify({"message": "Secret updated"})
    # if the secret wasn't found
    return jsonify({"error": "Secret not found"}), 404


