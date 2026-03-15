from flask import Flask, request, jsonify

from SinBlockchain import SinBlockchain
from Transaction import Transaction

app = Flask(__name__)

blockchain = SinBlockchain()


@app.route("/blocks", methods=["GET"])
def get_blocks():
    return jsonify([b.__dict__ for b in blockchain.chain])


@app.route("/transaction", methods=["POST"])
def add_transaction():

    data = request.json

    if not data:
        return {"error": "missing data"}, 400

    tx = Transaction(
        data["from"],
        data["to"],
        data["amount"]
    )

    blockchain.add_transaction(tx)

    return {"message": "Transaction added to SinPool"}


@app.route("/mine", methods=["GET"])
def mine():

    block = blockchain.mine_transactions()

    return {
        "message": "Block mined",
        "index": block.index,
        "hash": block.hash
    }


@app.route("/validate", methods=["GET"])
def validate():

    return {"valid": blockchain.is_valid()}


if __name__ == "__main__":

    print("SinNode running on http://localhost:5000")

    app.run(port=5000)
