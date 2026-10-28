from flask import Flask, render_template

from models.Product import Product
from models.ProductModel import ProductModel

app = Flask(__name__)

categories = {
    "all": {
        "name": "Всі фрукти",
        "icon": "https://cdn.jsdelivr.net/gh/jdecked/twemoji@latest/assets/72x72/1f34e.png",
    },
    "Ягоди": {
        "name": "Ягоди",
        "icon": "https://cdn.jsdelivr.net/gh/jdecked/twemoji@latest/assets/72x72/1f353.png",
    },
    "Цитрусові": {
        "name": "Цитрусові",
        "icon": "https://cdn.jsdelivr.net/gh/jdecked/twemoji@latest/assets/72x72/1f34a.png",
    },
    "Кісточкові": {
        "name": "Кісточкові",
        "icon": "https://cdn.jsdelivr.net/gh/jdecked/twemoji@latest/assets/72x72/1f352.png",
    },
    "Тропічні": {
        "name": "Тропічні",
        "icon": "https://cdn.jsdelivr.net/gh/jdecked/twemoji@latest/assets/72x72/1f34d.png",
    },
    "Яблука та груші": {
        "name": "Яблука та груші",
        "icon": "https://cdn.jsdelivr.net/gh/jdecked/twemoji@latest/assets/72x72/1f350.png",
    },
}


new_product = Product("Mango", "https://images.unsplash.com/photo-1553279768-865429fa0078?auto=format&fit=crop&w=800&q=85", 35, 4.9)
ProductModel.create_product(new_product)


@app.route('/')
def index():
    products = ProductModel.get_all_products()
    return render_template('index.html', categories=categories, products=products)

@app.route('/product/<int:id>')
def product_by_id(id):
    product = ProductModel.get_product_by_id(id)

    if not product:
        return "Product not found", 404

    return render_template('product.html', product=product)

if __name__ == "__main__":
    app.run(debug=True)
