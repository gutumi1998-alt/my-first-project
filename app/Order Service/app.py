from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

USER_SERVICE_URL = os.getenv("USER_SERVICE_URL")

orders = {
    101: {"order_id": 101, "user_id": 1, "item": "Laptop"}
}

@app.route("/orders/<int:order_id>")
def get_order(order_id):
    order = orders.get(order_id)
    user = requests.get(f"{USER_SERVICE_URL}/users/{order['user_id']}").json()

    return jsonify({
        "order": order,
        "user": user
    })

app.run(host="0.0.0.0", port=5002)
