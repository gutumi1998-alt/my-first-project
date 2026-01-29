from flask import Flask, jsonify

app = Flask(__name__)

# Fake database
users = {
    1: {"id": 1, "name": "Rakshitha"},
    2: {"id": 2, "name": "DevOps User"}
}

@app.route("/users/<int:user_id>")
def get_user(user_id):
    user = users.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
