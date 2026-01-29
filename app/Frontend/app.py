from flask import Flask
import requests

app = Flask(__name__)
BACKEND_URL = "http://order-service:5002/orders/101"

@app.route("/")
def home():
    data = requests.get(BACKEND_URL).json()
    return f"<h1>Order</h1><pre>{data}</pre>"

app.run(host="0.0.0.0", port=5000)
