from flask import Flask, render_template, request
import json
import csv
import sqlite3
import os

app = Flask(__name__)

# Function to create and populate the database if it doesn't exist
def create_database():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            price REAL NOT NULL
        )
    ''')
    
    # Check if data already exists
    cursor.execute('SELECT COUNT(*) FROM Products')
    if cursor.fetchone()[0] == 0:
        cursor.execute('''
            INSERT INTO Products (id, name, category, price)
            VALUES
            (1, 'Laptop', 'Electronics', 799.99),
            (2, 'Coffee Mug', 'Home Goods', 15.99)
        ''')
    
    conn.commit()
    conn.close()

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
        conn.row_factory = sqlite3.Row  # This enables column access by name
        cursor = conn.cursor()
        
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        
        # Convert rows to dictionaries
        products = []
        for row in rows:
            products.append({
                'id': row['id'],
                'name': row['name'],
                'category': row['category'],
                'price': row['price']
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

# Ensure the database exists when the app starts
@app.before_first_request
def before_first_request():
    create_database()

if __name__ == '__main__':
    # Create the database
    create_database()
    
    # Make sure templates directory exists
    if not os.path.exists('templates'):
        os.makedirs('templates')
    
    # Create template file if it doesn't exist
    template_path = os.path.join('templates', 'product_display.html')
    if not os.path.exists(template_path):
        with open(template_path, 'w') as f:
            f.write('''
<!DOCTYPE html>
<html>
<head>
    <title>Product Display</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid #ddd;
            padding: 8px;
        }
        tr:nth-child(even) {
            background-color: #f2f2f2;
        }
        th {
            padding-top: 12px;
            padding-bottom: 12px;
            text-align: left;
            background-color: #4CAF50;
            color: white;
        }
    </style>
</head>
<body>
    <h1>Products</h1>
    <table>
        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Category</th>
            <th>Price</th>
        </tr>
        {% for product in products %}
        <tr>
            <td>{{ product.id }}</td>
            <td>{{ product.name }}</td>
            <td>{{ product.category }}</td>
            <td>${{ product.price }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
            ''')
    
    # Create sample JSON file if it doesn't exist
    if not os.path.exists('products.json'):
        with open('products.json', 'w') as f:
            json.dump([
                {"id": 1, "name": "Laptop", "category": "Electronics", "price": 799.99},
                {"id": 2, "name": "Coffee Mug", "category": "Home Goods", "price": 15.99}
            ], f)
    
    # Create sample CSV file if it doesn't exist
    if not os.path.exists('products.csv'):
        with open('products.csv', 'w') as f:
            writer = csv.writer(f)
            writer.writerow(['id', 'name', 'category', 'price'])
            writer.writerow([1, 'Laptop', 'Electronics', 799.99])
            writer.writerow([2, 'Coffee Mug', 'Home Goods', 15.99])
    
    app.run(debug=True)