"""
Secret sharing routes.
"""
import secrets
from flask import Blueprint, jsonify
from datetime import datetime, timezone
from flask_jwt_extended import (jwt_required, get_jwt_identity)
from models.share_token import ShareToken
from utils.encryption import decrypt_secret
from utils.file_db import (TOKENS_FILE, SECRETS_FILE, load_data, save_data)
from utils.logger import log_event


share_bp = Blueprint("share", __name__)


@share_bp.route("/secrets/<int:secret_id>/share", methods=["POST"])
@jwt_required()
def create_share_link(secret_id):
    """
     Generate one-time shareable link.
    """
    user_id = int(get_jwt_identity())
    secrets_data = load_data(SECRETS_FILE)
    # Verify secret ownership
    target_secret = None
    for secret in secrets_data:
        if secret["id"] == secret_id and secret["user_id"] == user_id:
            target_secret = secret
            break
    # if the secret doesn't exist
    if not target_secret:
        return jsonify({"error": "Secret not found"}), 404

    # if the secret was found - generates  the link for sharing
    token = secrets.token_urlsafe(32)
    share_token = ShareToken(
        token=token,
        secret_id=secret_id)
    tokens = load_data(TOKENS_FILE)
    tokens.append(share_token.to_dict())
    save_data(TOKENS_FILE, tokens)
    # add log
    log_event(
        f"User {user_id} generated share token for secret {secret_id}"
    )
    return jsonify({"share_link": f"/share/{token}"})


@share_bp.route("/share/<token>", methods=["GET"])
def access_shared_secret(token):
    """
     Access shared secret using one-time token.
     """
    tokens = load_data(TOKENS_FILE)
    secrets_data = load_data(SECRETS_FILE)
    for token_data in tokens:
        if token_data["token"] == token:
            # Check if token already used
            if token_data["used"]:
                return jsonify({"error": "Token already used"}), 400

            # Check expiration
            expiration = datetime.fromisoformat(token_data["expires_at"])
            if datetime.now(timezone.utc) > expiration:
                return jsonify({"error": "Token expired"}), 400

            # Find secret
            for secret in secrets_data:
                if secret["id"] == token_data["secret_id"]:
                    # Mark token as used
                    token_data["used"] = True
                    save_data(TOKENS_FILE, tokens)
                    # add log
                    log_event(
                        f"Shared secret {secret['id']} accessed using token"
                    )
                    return jsonify({"secret": decrypt_secret(secret["encrypted_value"])})

    # if the code reached here - the token is invalid
    return jsonify({"error": "Invalid token"}), 404
