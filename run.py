from flask import Flask

from app import home_bp
from app.products.routes import products_bp
from app.users.routes import users_bp


def create_app():
    app = Flask(__name__)
    app.register_blueprint(home_bp)
    app.register_blueprint(products_bp)
    app.register_blueprint(users_bp)
    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
