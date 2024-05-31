#!/usr/bin/python3
"""API security and authentication techniques."""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your_secret_key'

auth = HTTPBasicAuth()
jwt = JWTManager(app)

# User data with hashed passwords and roles
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password1"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password2"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Verify the username and password."""
    if username in users and check_password_hash(
            users[username]['password'], password):
        return username


@app.route('/login', methods=['POST'])
def login():
    """Endpoint for user login."""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        access_token = create_access_token(identity=username)
        return jsonify({"access_token": access_token})

    return jsonify({"error": "Invalid credentials"}), 401


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    """Endpoint protected by basic authentication."""
    return jsonify(message="Basic Auth: Access Granted")


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """Endpoint protected by JWT authentication."""
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Endpoint accessible only to admins."""
    current_user = get_jwt_identity()
    user = users.get(current_user)
    if user and user["role"] == "admin":
        return "Admin Access: Granted"
    else:
        return jsonify({"error": "Forbidden"}), 403


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Handler for unauthorized access."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Handler for invalid tokens."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Handler for expired tokens."""
    return jsonify({"error": "Token has expired"}), 401


if __name__ == "__main__":
    app.run(debug=True, port=5001)
