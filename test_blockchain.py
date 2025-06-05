from blockchain import Blockchain

def main():
    # Initialize the blockchain
    my_blockchain = Blockchain()

    # Adding some blocks with arbitrary data
    my_blockchain.add_block("First block data")
    my_blockchain.add_block("Second block data")
    my_blockchain.add_block("Third block data")

    # Print the blockchain
    for block in my_blockchain.chain:
        print(f"Index: {block.index}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Hash: {block.hash}")
        print(f"Nonce: {block.nonce}")
        print("-" * 30)

    # Validate the blockchain
    if my_blockchain.is_valid():
        print("Blockchain is valid.")
    else:
        print("Blockchain is invalid.")

if __name__ == "__main__":
    main()
