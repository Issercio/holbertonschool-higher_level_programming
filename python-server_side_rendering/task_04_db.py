from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

def read_json_data():
    with open('products.json', 'r') as f:
        return json.load(f)

def read_csv_data():
    products = []
    with open('products.csv', 'r') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['price'] = float(row['price'])
            products.append(row)
    return products

def read_sql_data():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, name, category, price FROM Products')
    rows = cursor.fetchall()
    
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

@app.route('/products')
def display_products():
    source = request.args.get('source', '')
    
    try:
        if source == 'json':
            products = read_json_data()
        elif source == 'csv':
            products = read_csv_data()
        elif source == 'sql':
            products = read_sql_data()
        else:
            return "Wrong source"
        
        return render_template('product_display.html', products=products)
    except Exception as e:
        if source == 'json':
            return "Error: JSON file not found or invalid"
        elif source == 'csv':
            return "Error: CSV file not found or invalid"
        elif source == 'sql':
            return "Error: Database error occurred"
        else:
            return "Wrong source"

if __name__ == '__main__':
    try:
        # Create and populate the database
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        
        # Create table
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
    except Exception as e:
        print(f"Database initialization error: {e}")
    
    app.run(debug=True)