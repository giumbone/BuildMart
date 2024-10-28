from flask import Flask, render_template, request, redirect, url_for, flash
import os

app = Flask(__name__)

DATABASE_URI = os.getenv("DATABASE_URI")
SECRET_KEY = os.getenv("SECRET_KEY")

app.config['SECRET_KEY'] = SECRET_KEY

products_db = [
    {"id": 1, "name": "Product 1", "price": 100},
    {"id": 2, "name": "Product 2", "price": 200}
]

@app.route('/')
def home():
    return render_template('index.html', products=products_db)

@app.route('/product/<int:product_id>')
def product(product_id):
    product = next((item for item in products_db if item["id"] == product_id), None)
    if product:
        return render_template('product_detail.html', product=product)
    else:
        return "Product not found", 404

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        new_product_name = request.form.get('product_name')
        new_product_price = request.form.get('product_price')
        
        if new_product_name and new_product_price:
            new_product_id = len(products_db) + 1
            products_db.append({
                "id": new_product_id,
                "name": new_product_name,
                "price": float(new_product_price)
            })
            flash('New product added successfully!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Product name and price are required!', 'error')
        
    return render_template('add_product.html')

if __name__ == '__main__':
    app.run(debug=True)