from flask import Flask , jsonify

app = Flask(__name__)

accounts =  {
        "1": {"balance": 1000},
        "2": {"balance": 500} }

@app.route("/account/<user_id>")

def account(user_id):
    if user_id in accounts:
        return jsonify(accounts[user_id])
    return jsonify({"error": "User not found"}), 404

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)

