from flask import Flask, render_template, request

import sqlite3

app = Flask(__name__)

# Function to fetch product data from SQLite database
def get_products_from_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()
    conn.close()
    return products

# Route to display product data based on source query parameter
@app.route('/products')
def display_products():
    source = request.args.get('source', default='')

    if source == 'sql':
        products = get_products_from_db()
        return render_template('product_display.html', products=products)
    else:
        return render_template('error.html', message='Wrong source')

if __name__ == '__main__':
    app.run(debug=True)
