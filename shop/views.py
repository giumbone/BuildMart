from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

DATABASE_URI = os.getenv("DATABASE_URI")
SECRET_KEY = os.getenv("SECRET_KEY")

app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def home():
    products = [{"name": "Product 1", "price": 100}, {"name": "Product 2", "price": 200}]
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = {"id": product_id, "name": f"Product {product_id}", "description": "Product Description", "price": 100*product_id}
    return render_template('product_detail.html', product=product)

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        return redirect(url_for('home'))
    return render_template('add_product.html')

if __name__ == '__main__':
    app.run(debug=True)