#!/usr/bin/python3
"""Model of basic_security."""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    JWTManager, create_access_token, jwt_required, get_jwt_identity
)

app = Flask(__name__)
auth = HTTPBasicAuth()

# Clé secrète pour JWT
app.config["JWT_SECRET_KEY"] = "supersecretkey"
jwt = JWTManager(app)

# Base de données simulée (en mémoire)
users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


# 🛡 Basic Authentication
@auth.verify_password
def verify_password(username, password):
    """Vérifie le mot de passe avec Basic Auth."""
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username  # Authentification réussie
    return None


# 🔒 Route protégée par Basic Auth
@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """Route accessible avec Basic Auth."""
    return "Basic Auth: Access Granted", 200


# 🔑 Route de connexion pour JWT
@app.route("/login", methods=["POST"])
def login():
    """Génère un JWT après connexion."""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid username or password"}), 401

    # Générer un JWT avec le rôle de l'utilisateur
    access_token = create_access_token(
        identity={"username": username, "role": user["role"]}
    )
    return jsonify({"access_token": access_token}), 200


# 🔒 Route protégée par JWT
@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    """Route accessible uniquement avec un JWT valide."""
    return "JWT Auth: Access Granted", 200


# 🔑 Route protégée pour Admin uniquement
@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """Route réservée aux administrateurs."""
    current_user = get_jwt_identity()
    if current_user["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted", 200


# 🛑 Gestion des erreurs JWT
@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Gère l'erreur JWT lorsque le token est manquant ou invalide."""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Gère l'erreur JWT lorsque le token est invalide."""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """Gère l'erreur JWT lorsque le token a expiré."""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """Gère l'erreur JWT lorsque le token a été révoqué."""
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """Gère l'erreur JWT lorsque le token doit être frais."""
    return jsonify({"error": "Fresh token required"}), 401


# 🚀 Lancer le serveur
if __name__ == "__main__":
    app.run(debug=True)
