from flask import Flask, render_template, request
import json
import csv

app = Flask(__name__)

# 📌 Fonction pour lire le fichier JSON
def read_json_file():
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except Exception as e:
        return {"error": f"Erreur de lecture JSON: {str(e)}"}

# 📌 Fonction pour lire le fichier CSV
def read_csv_file():
    try:
        products = []
        with open("products.csv", "r") as file:
            csv_reader = csv.DictReader(file)
            for row in csv_reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
        return products
    except Exception as e:
        return {"error": f"Erreur de lecture CSV: {str(e)}"}

# 📌 Route principale
@app.route("/products")
def show_products():
    source = request.args.get("source")  # Récupérer ?source=json ou ?source=csv
    product_id = request.args.get("id")  # Récupérer ?id=1

    # Sélectionner la source des données
    if source == "json":
        products = read_json_file()
    elif source == "csv":
        products = read_csv_file()
    else:
        return render_template("product_display.html", error="⚠️ Mauvaise source ! Utilisez ?source=json ou ?source=csv.")

    # Vérifier si les données sont valides
    if isinstance(products, dict) and "error" in products:
        return render_template("product_display.html", error=products["error"])

    # Si un ID est fourni, filtrer les résultats
    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products if p["id"] == product_id]
            if not filtered_products:
                return render_template("product_display.html", error="❌ Produit non trouvé.")
            products = filtered_products
        except ValueError:
            return render_template("product_display.html", error="⚠️ ID invalide !")

    return render_template("product_display.html", products=products)

# Lancer l'application Flask
if __name__ == "__main__":
    app.run(debug=True, port=5000)
