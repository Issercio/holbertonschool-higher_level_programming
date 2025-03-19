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
                # Make sure all expected keys are present
                if all(key in row for key in ['id', 'name', 'category', 'price']):
                    # Convert price to float and id to int
                    row['price'] = float(row['price'])
                    row['id'] = int(row['id'])
                    products.append(row)
        return products
    except (FileNotFoundError, csv.Error):
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
    except sqlite3.Error as e:
        # More specific error handling
        print(f"Database error: {e}")
        return None

@app.route('/products')
def display_products():
    source = request.args.get('source', '')
    
    # Determine data source and fetch data
    products = None
    error_message = None
    
    if source == 'json':
        products = read_json_data()
        if products is None:
            error_message = "Error: JSON file not found or invalid"
    elif source == 'csv':
        products = read_csv_data()
        if products is None:
            error_message = "Error: CSV file not found or invalid"
    elif source == 'sql':
        products = read_sql_data()
        if products is None:
            error_message = "Error: Database error occurred"
    else:
        return "Wrong source"
    
    # Return error message if products is None
    if error_message:
        return error_message
    
    # Render template with the products data
    return render_template('product_display.html', products=products)

if __name__ == '__main__':
    # Create the database if it doesn't exist
    try:
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
        
        # Check if data exists
        cursor.execute('SELECT COUNT(*) FROM Products')
        if cursor.fetchone()[0] == 0:
            # Insert sample data
            cursor.execute('''
                INSERT INTO Products (id, name, category, price)
                VALUES
                (1, 'Laptop', 'Electronics', 799.99),
                (2, 'Coffee Mug', 'Home Goods', 15.99)
            ''')
            conn.commit()
        
        conn.close()
    except sqlite3.Error as e:
        print(f"Database initialization error: {e}")
    
    app.run(debug=True)