from flask import jsonify


def view_products(myapp):
    @myapp.route("/products")
    def products():
        product_lists = [
            {
                "fruits": ["Apples", "Avocado", "Banana"],
                "bevarages": ["Club soda", "Coke", "Juice"],
            }
        ]

        return jsonify(product_lists)
