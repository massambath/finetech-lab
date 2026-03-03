from flask import Flask, jsonify, request
import time
import random

app = Flask(__name__)

@app.route("/transfer", methods=["POST"])
def transfer():
    time.sleep(random.uniform(0.05,0.5)) #simule latence
    data = request.json
    return jsonify({
        "status": "success",
        "from": data["fromUser"],
        "to": data["toUser"],
        "amount": data["amount"]
        })

if __name__ =="__main__":
    app.run(host="0.0.0.0", port= 5002)

