from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_data():
    """Read product data from JSON file"""
    try:
        with open('products.json', 'r') as f:
            data = json.load(f)
            return data
    except Exception:
        return None

def read_csv_data():
    """Read product data from CSV file"""
    try:
        products = []
        with open('products.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Ensure price is a float
                row['price'] = float(row['price'])
                products.append(row)
        return products
    except Exception:
        return None

def read_sql_data():
    """Read product data from SQLite database"""
    try:
        # Connect to the database
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        
        # Execute the query
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        
        # Format the data
        products = []
        for row in rows:
            product = {
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            }
            products.append(product)
        
        conn.close()
        return products
    except sqlite3.Error:
        # Specific error handling for SQLite
        return None

@app.route('/products')
def display_products():
    """Display products from the selected data source"""
    # Get the source from query parameters
    source = request.args.get('source', '')
    
    # Determine which data source to use
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
        # Invalid source
        return "Wrong source"
    
    # Render the template with product data
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)