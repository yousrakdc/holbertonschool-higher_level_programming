#!/usr/bin/env python3
# task_04_flask.py

from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory storage for users
users = {}


# Root endpoint
@app.route("/")
def home():
    return "Welcome to the Flask API!"


# Endpoint to get all usernames
@app.route("/data", methods=["GET"])
def get_usernames():
    usernames = list(users.keys())
    return jsonify(usernames)


# Endpoint to get user details
@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


# Endpoint to add a new user
@app.route("/add_user", methods=["POST"])
def add_user():
    user_data = request.get_json()
    username = user_data.get("username")

    if username in users:
        return jsonify({"error": "User already exists"}), 409

    users[username] = user_data
    return jsonify({"message": "User added", "user": user_data}), 201


# Endpoint to check status
@app.route("/status", methods=["GET"])
def get_status():
    return "OK"


if __name__ == "__main__":
    app.run()
