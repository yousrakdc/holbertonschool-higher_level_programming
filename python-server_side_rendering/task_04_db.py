from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# Function to read data from SQLite database
def read_sqlite_data():
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

@app.route('/products')
def products():
    source = request.args.get('source')

    if source == 'json':
        with open('products.json', 'r') as f:
            data = json.load(f)
    elif source == 'csv':
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            data = [{
                "id": int(row["id"]),
                "name": row["name"],
                "category": row["category"],
                "price": float(row["price"])
            } for row in reader]
    elif source == 'sql':
        try:
            data = read_sqlite_data()
        except sqlite3.Error as e:
            return render_template('product_display.html', error=f"SQLite Error: {str(e)}")
    else:
        return render_template('product_display.html', error="Wrong source")

    return render_template('product_display.html', products=data)

if __name__ == '__main__':
    app.run(debug=True)
