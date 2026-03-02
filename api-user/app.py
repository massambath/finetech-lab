from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

@app.route("/balance/<user_id>")
def balance(user_id):
    try:
        r = requests.get(f"http://service-accoun:5001/account/{user_id}")
        return jsonify(r.json())
    except :
        return jsonify({"error": "Service Account unreachable"}), 500

@app.route("/transfer", methods=["POST"])
def transfer():
    try:
        r = requests.post("http://service-payment:5002/transfer", json=request.json)
        return jsonify(r.json())
    except:
        return jsonify({"error":"Payment service unreachable"}), 500

if __name__ = "__main__":
    app.run(host="0.0.0.0", port=5000)

