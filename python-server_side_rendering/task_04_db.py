from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# Function to read data from JSON file
def read_json_file(filename):
    with open(filename, 'r') as f:
        return json.load(f)

# Function to read data from CSV file
def read_csv_file(filename):
    products = []
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            products.append({
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            })
    return products

# Function to fetch product data from SQLite database
def get_products_from_db():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM Products')
        products = cursor.fetchall()
        conn.close()
        return [{
            "id": product[0],
            "name": product[1],
            "category": product[2],
            "price": float(product[3])
        } for product in products]
    except sqlite3.Error as e:
        print(f"SQLite error occurred: {e}")
        return None

@app.route('/products')
def products():
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source == 'json':
        data = read_json_file('products.json')
    elif source == 'csv':
        data = read_csv_file('products.csv')
    elif source == 'sql':
        data = get_products_from_db()
        if data is None:
            return render_template('product_display.html', error="Database error occurred")
    else:
        return render_template('product_display.html', error="Wrong source")

    if product_id:
        try:
            product_id = int(product_id)
            data = [product for product in data if product['id'] == product_id]
            if not data:
                return render_template('product_display.html', error="Product not found")
        except ValueError:
            return render_template('product_display.html', error="Invalid product id")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True)
