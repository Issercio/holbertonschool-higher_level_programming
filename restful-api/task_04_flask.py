#!/usr/bin/python3
'''model of flask
'''

from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionnaire pour stocker les utilisateurs
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles",
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York",
    },
}


# 📌 Route principale "/"
@app.route("/")
def home():
    return "Welcome to the Flask API!"


# 📌 Endpoint "/status"
@app.route("/status")
def status():
    return "OK"


# 📌 Endpoint "/data" pour afficher tous les usernames
@app.route("/data")
def get_usernames():
    return jsonify(list(users.keys()))  # Retourne seulement les usernames


# 📌 Endpoint "/users/<username>" pour afficher un utilisateur spécifique
@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


# 📌 Endpoint "/add_user" pour ajouter un nouvel utilisateur via POST
@app.route("/add_user", methods=["POST"])
def add_user():
    data = request.get_json()

    if not data or "username" not in data:
        return jsonify(
            {"error": "Username is required"}
        ), 400  # Erreur si username absent

    username = data["username"]

    if username in users:
        return jsonify(
            {"error": "User already exists"}
        ), 400  # Erreur si utilisateur existe déjà

    users[username] = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", ""),
    }

    return jsonify(
        {"message": "User added", "user": users[username]}
    ), 201  # 201 = Created


# 📌 Lancer l'application Flask
if __name__ == "__main__":
    app.run(debug=True)  # Mode debug activé
