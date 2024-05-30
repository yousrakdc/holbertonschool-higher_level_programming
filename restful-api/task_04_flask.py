#!/usr/bin/env python3
from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory data store
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}


@app.route('/')
def home():
    """Root endpoint that returns a welcome message."""
    return "Welcome to the Flask API!"


@app.route('/data', methods=['GET'])
def get_users():
    """Endpoint to get the list of all users."""
    user_list = [user for user in users.values()]
    return jsonify(user_list)


@app.route('/status', methods=['GET'])
def get_status():
    """Endpoint to check the API status."""
    return jsonify({"status": "OK"})


@app.route('/users/<username>', methods=['GET'])
def get_user(username):
    """Endpoint to get details of a specific user by username."""
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Endpoint to add a new user."""
    user_data = request.get_json()
    username = user_data.get('username')
    if not username:
        return jsonify({"error": "Username is required"}), 400
    if username in users:
        return jsonify({"error": "User already exists"}), 409
    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201


if __name__ == '__main__':
    app.run(debug=True)
