from . import products_bp
from flask import jsonify


@products_bp.route("/products")
def products():
    product_lists = [
        {
            "fruits": ["Apples", "Avocado", "Banana"],
            "bevarages": ["Club soda", "Coke", "Juice"],
        }
    ]

    return jsonify(product_lists)
