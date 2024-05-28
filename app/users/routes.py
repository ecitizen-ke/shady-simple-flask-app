from flask import jsonify
from . import users_bp


@users_bp.route("/users")
def get_users():
    credentials = [
        {"username": "admin", "password": "admin123"},
        {"username": "Soi", "password": "123456"},
    ]
    return jsonify(credentials)
