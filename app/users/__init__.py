from flask import Blueprint, jsonify

users_bp = Blueprint("users_bp", __name__)


@users_bp.route("/users")
def get_users():
    credentials = [
        {"username": "admin", "password": "admin123"},
        {"username": "Soi", "password": "123456"},
    ]
    return jsonify(credentials)
