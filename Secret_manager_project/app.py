"""
Main Flask application.
"""
from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from routes.auth import auth_bp
from routes.secrets import secret_bp
from routes.share import share_bp

app = Flask(__name__)

# Load configuration
app.config.from_object(Config)
# Initialize JWT manager
JWTManager(app)
# Register route blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(secret_bp)
app.register_blueprint(share_bp)

@app.route("/")
def home():
    """
     Health check endpoint.
     """
    return {"message": "Secure Secrets Manager Running"}


if __name__ == "__main__":
    app.run(debug=True)
