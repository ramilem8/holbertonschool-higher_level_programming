from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    jwt_required,
    get_jwt_identity
)
from werkzeug.security import (
    generate_password_hash,
    check_password_hash
)

app = Flask(__name__)

# JWT Secret Key
app.config["JWT_SECRET_KEY"] = "super-secret-key"

# Extensions
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Users
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


@jwt.unauthorized_loader
def unauthorized_callback(error):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def invalid_token_callback(error):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify({"error": "Token has expired"}), 401


@auth.verify_password
def verify_password(username, password):

    if username in users:
        stored_password = users[username]["password"]

        if check_password_hash(stored_password, password):
            return username

    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():

    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username not in users:
        return jsonify({"error": "Bad credentials"}), 401

    user = users[username]

    if not check_password_hash(user["password"], password):
        return jsonify({"error": "Bad credentials"}), 401

   
    access_token = create_access_token(
        identity={
            "username": username,
            "role": user["role"]
        }
    )

    return jsonify({
        "access_token": access_token
    })


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def admin_only():

    current_user = get_jwt_identity()

    if current_user["role"] != "admin":
        return jsonify({
            "error": "Admin access required"
        }), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
