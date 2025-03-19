from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

# Function to read data from JSON file
def read_json_data():
    try:
        with open('products.json', 'r') as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return None

# Function to read data from CSV file
def read_csv_data():
    try:
        products = []
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Convert price to float
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except FileNotFoundError:
        return None

# Function to read data from SQLite database
def read_sql_data():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        
        # Convert rows to dictionaries
        products = []
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        
        conn.close()
        return products
    except sqlite3.Error:
        return None

@app.route('/products')
def display_products():
    source = request.args.get('source', '')
    
    # Determine data source and fetch data
    if source == 'json':
        products = read_json_data()
        if products is None:
            return "Error: JSON file not found or invalid"
    elif source == 'csv':
        products = read_csv_data()
        if products is None:
            return "Error: CSV file not found or invalid"
    elif source == 'sql':
        products = read_sql_data()
        if products is None:
            return "Error: Database error occurred"
    else:
        return "Wrong source"
    
    # Render template with the products data
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)