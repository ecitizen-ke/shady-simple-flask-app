from flask import jsonify, Blueprint

products_bp = Blueprint("products_bp", __name__)


@products_bp.route("/products")
def products():
    product_lists = [
        {
            "fruits": ["Apples", "Avocado", "Banana"],
            "bevarages": ["Club soda", "Coke", "Juice"],
        }
    ]

    return jsonify(product_lists)
