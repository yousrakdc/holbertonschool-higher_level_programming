#!/usr/bin/env python3
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
    if username in users and check_password_hash(
            users[username]['password'], password):
        return username
    return None


@app.route('/login', methods=['POST'])
def login():
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)

    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    user = users.get(username, None)
    if user and check_password_hash(user['password'], password):
        access_token = create_access_token(
            identity={"username": username, "role": user["role"]}
        )
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"msg": "Bad username or password"}), 401


@app.route('/basic-protected')
@auth.login_required
def basic_protected():
    return jsonify(message="Basic Auth: Access Granted")


@app.route('/jwt-protected')
@jwt_required()
def jwt_protected():
    current_user = get_jwt_identity()
    return jsonify(message="JWT Auth: Access Granted", user=current_user)


def role_required(role):
    def wrapper(fn):
        @jwt_required()
        def decorator(*args, **kwargs):
            claims = get_jwt_identity()
            if claims['role'] != role:
                return jsonify(msg='Unauthorized'), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper


@app.route('/admin-only')
@role_required('admin')
def admin_only():
    return jsonify(message="Admin Access: Granted")


@jwt.unauthorized_loader
def unauthorized_response(callback):
    return jsonify({"msg": "Missing Authorization Header"}), 401


@jwt.invalid_token_loader
def invalid_token_response(callback):
    return jsonify({"msg": "Invalid token"}), 401


@jwt.expired_token_loader
def expired_token_response(callback):
    return jsonify({"msg": "Token has expired"}), 401


@jwt.revoked_token_loader
def revoked_token_response(callback):
    return jsonify({"msg": "Token has been revoked"}), 401


@jwt.claims_verification_failed_loader
def claims_verification_failed_response(callback):
    return jsonify({"msg": "Claims verification failed"}), 401


if __name__ == '__main__':
    app.run(debug=True)
