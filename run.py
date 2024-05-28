from flask import Flask
from app.users import view_users
from app.products import view_products
from app import home

app = Flask(__name__)
view_users(app)
view_products(app)
home(app)


if __name__ == "__main__":
    app.run(debug=True)
