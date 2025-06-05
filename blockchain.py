import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash, nonce=0):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        value = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(value.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_block(data='Genesis Block', previous_hash='0')  # Genesis block

    def create_block(self, data, previous_hash, nonce=0):
        index = len(self.chain)
        timestamp = time.time()
        block = Block(index, timestamp, data, previous_hash, nonce)
        self.chain.append(block)
        return block

    def add_block(self, data):
        nonce = 0
        while True:
            block = self.create_block(data, self.chain[-1].hash if self.chain else '0', nonce)
            if block.hash.startswith("0"):  # Proof-of-Work condition (one leading zero)
                print(f"Block added: {block.index} with hash: {block.hash}")
                break
            nonce += 1


    def is_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            # Check if the current block's hash is correct
            if current.hash != current.calculate_hash():
                return False

            # Check if the previous hash is correct
            if current.previous_hash != previous.hash:
                return False

        return True
