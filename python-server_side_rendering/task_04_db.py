from flask import Flask, render_template, request, jsonify
import json
import csv
import sqlite3

app = Flask(__name__)

# Fonction pour lire les données depuis le fichier JSON
def read_json_data():
    with open('products.json') as f:
        return json.load(f)

# Fonction pour lire les données depuis le fichier CSV
def read_csv_data():
    products = []
    with open('products.csv') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['price'] = float(row['price'])
            products.append(row)
    return products

# Fonction pour lire les données depuis la base de données SQLite
def read_sql_data():
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        
        products = []
        for row in rows:
            product = {'id': row[0], 'name': row[1], 'category': row[2], 'price': row[3]}
            products.append(product)
        
        conn.close()
        return products
    except sqlite3.Error as e:
        return None  # Erreur de connexion à la base de données

# Route pour afficher les produits
@app.route('/products')
def display_products():
    source = request.args.get('source')  # Paramètre de source (json, csv, sql)
    product_id = request.args.get('id', type=int)  # Paramètre optionnel id

    # Lire les données selon la source spécifiée
    if source == 'json':
        products = read_json_data()
    elif source == 'csv':
        products = read_csv_data()
    elif source == 'sql':
        products = read_sql_data()
        if products is None:
            return render_template('product_display.html', error="Database error")
    else:
        return render_template('product_display.html', error="Wrong source")

    # Filtrer les produits par id si fourni
    if product_id:
        products = [product for product in products if product['id'] == product_id]
        if not products:
            return render_template('product_display.html', error="Product not found")

    # Rendre le template avec les produits filtrés
    return render_template('product_display.html', products=products)

# Lancer l'application Flask
if __name__ == '__main__':
    app.run(debug=True)
