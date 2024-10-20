from flask import Flask, render_template


# Sample data for products
product_list = [
    {"id": 1, "name": "Laptop", "category": "Electronics", "price": 1200},
    {"id": 2, "name": "Smartphone", "category": "Electronics", "price": 800},
    {"id": 3, "name": "T-shirt", "category": "Clothing", "price": 20},
    {"id": 4, "name": "Jeans", "category": "Clothing", "price": 50},
    {"id": 5, "name": "Blender", "category": "Home Appliances", "price": 60},
]


app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", products=product_list)

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)