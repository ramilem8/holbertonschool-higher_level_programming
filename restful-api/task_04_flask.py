from flask import Flask, jsonify, request

app = Flask(__name__)

# Users dictionary
users = {}


# Home endpoint
@app.route("/")
def home():
    return "Welcome to the Flask API!"


# Status endpoint
@app.route("/status")
def status():
    return "OK"


# Data endpoint
@app.route("/data")
def get_data():
    return jsonify(list(users.keys()))


# Get specific user
@app.route("/users/<username>")
def get_user(username):

    if username in users:
        return jsonify(users[username])

    return jsonify({"error": "User not found"}), 404


# Add new user
@app.route("/add_user", methods=["POST"])
def add_user():

    # JSON yoxlaması
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json()

    # username yoxlaması
    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    # duplicate username yoxlaması
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # user əlavə et
    users[username] = data

    return jsonify({
        "message": "User added",
        "user": data
    }), 201


# Run server
if __name__ == "__main__":
    app.run()