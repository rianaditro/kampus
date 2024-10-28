from flask import Flask, request, jsonify, url_for

app = Flask(__name__)

# Sample data for products
product_list = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 1200},
    {"id": 2, "name": "Smartphone", "category": "Electronics", "price": 800},
    {"id": 3, "name": "T-shirt", "category": "Clothing", "price": 20},
    {"id": 4, "name": "Jeans", "category": "Clothing", "price": 50},
    {"id": 5, "name": "Blender", "category": "Home Appliances", "price": 60},
]


@app.route("/products/<int:product_id>")
def products(product_id:int):
    for product in product_list:
        if product["id"] == product_id:
            return jsonify(product)
        else:
            product = None

    if product is None:
        return jsonify({"error": "Product not found"}), 404


@app.route("/")
def index():
    url_list = ""
    for product in product_list:
        url = f"<a href='{url_for('products', product_id=product['id'])}'>{product['name']}</a><br>"
        url_list += url
    return url_list

@app.route("/search")
def search():
    query = request.args.get('category')  # Get 'query' parameter from the URL
    product_urls = ""

    for product in product_list:
        if product["category"].lower() == query.lower():
            product_urls += f"<a href='{url_for('products', product_id=product['id'])}'>{product['name']}</a><br>"

    return product_urls



if __name__ == "__main__":
    app.run(debug=True)