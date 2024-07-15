from flask import Flask, render_template, request, jsonify
import sqlite3
import csv

app = Flask(__name__)

# Function to fetch data from SQLite database
def fetch_data_from_sqlite():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    data = cursor.fetchall()
    conn.close()
    return data

# Function to fetch data from JSON file (assuming data.json exists)
def fetch_data_from_json():
    # Replace with actual JSON data loading logic
    return []

# Function to fetch data from CSV file (assuming data.csv exists)
def fetch_data_from_csv():
    # Replace with actual CSV data loading logic
    return []

# Route to handle displaying products
@app.route('/products')
def display_products():
    source = request.args.get('source')

    if source == 'json':
        data = fetch_data_from_json()
    elif source == 'csv':
        data = fetch_data_from_csv()
    elif source == 'sql':
        data = fetch_data_from_sqlite()
    else:
        return render_template('error.html', message='Wrong source')

    return render_template('product_display.html', products=data)

# Error handling for database-related issues
@app.errorhandler(sqlite3.Error)
def handle_database_error(error):
    return render_template('error.html', message='Database error: {}'.format(error))

if __name__ == '__main__':
    app.run(debug=True)
