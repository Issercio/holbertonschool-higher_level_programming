from flask import Flask, render_template, request, json, jsonify
import csv

app = Flask(__name__)

# Function to read data from JSON file
def read_json():
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except Exception as e:
        return []

# Function to read data from CSV file
def read_csv():
    try:
        with open("products.csv", "r") as file:
            csv_reader = csv.DictReader(file)
            return [{"id": int(row["id"]), "name": row["name"], "category": row["category"], "price": float(row["price"])} for row in csv_reader]
    except Exception as e:
        return []

@app.route("/products")
def products():
    source = request.args.get("source")
    product_id = request.args.get("id", type=int)

    if source == "json":
        data = read_json()
    elif source == "csv":
        data = read_csv()
    else:
        return render_template("product_display.html", error="Wrong source. Use 'json' or 'csv'.")

    # If ID is provided, filter the data
    if product_id:
        data = [item for item in data if item["id"] == product_id]
        if not data:
            return render_template("product_display.html", error=f"Product with ID {product_id} not found.")

    return render_template("product_display.html", products=data)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
