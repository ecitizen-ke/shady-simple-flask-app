from flask import jsonify


def view_users(myapp):
    @myapp.route("/users")
    def get_users():
        credentials = [
            {"username": "admin", "password": "admin123"},
            {"username": "Soi", "password": "123456"},
        ]
        return jsonify(credentials)
