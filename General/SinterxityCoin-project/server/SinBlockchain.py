import json
import time
import os

from Block import Block
from Transaction import Transaction


class SinBlockchain:

    def __init__(self):

        self.difficulty = 2
        self.SinPool = []

        self.data_path = "../data/sinchain.json"

        if os.path.exists(self.data_path):
            self.load()
        else:
            self.chain = [self.create_genesis_block()]
            self.save()

    def create_genesis_block(self):

        print("Creating GenesisSin block")

        return Block(
            0,
            int(time.time()),
            [],
            "0"
        )

    def get_latest_block(self):
        return self.chain[-1]

    def add_transaction(self, transaction):
        self.SinPool.append(transaction.to_dict())
        self.save()

    def mine_transactions(self):

        reward = Transaction(
            "SinReward",
            "miner",
            50
        )

        self.SinPool.append(reward.to_dict())

        previous = self.get_latest_block()

        block = Block(
            previous.index + 1,
            int(time.time()),
            self.SinPool,
            previous.hash
        )

        block.mine_block(self.difficulty)

        self.chain.append(block)

        self.SinPool = []

        self.save()

        return block

    def is_valid(self):

        for i in range(1, len(self.chain)):

            current = self.chain[i]
            previous = self.chain[i-1]

            if current.hash != current.calculate_hash():
                return False

            if current.previous_hash != previous.hash:
                return False

        return True

    def save(self):

        data = {
            "chain": [block.__dict__ for block in self.chain],
            "SinPool": self.SinPool
        }

        os.makedirs("../data", exist_ok=True)

        with open(self.data_path, "w") as f:
            json.dump(data, f, indent=2)

    def load(self):

        with open(self.data_path) as f:
            data = json.load(f)

        self.chain = []

        for b in data["chain"]:
            block = Block(
                b["index"],
                b["timestamp"],
                b["data"],
                b["previous_hash"]
            )

            block.nonce = b["nonce"]
            block.hash = b["hash"]

            self.chain.append(block)

        self.SinPool = data["SinPool"]
