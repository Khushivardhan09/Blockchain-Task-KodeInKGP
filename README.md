# Blockchain-Task-KodeInKGP
This project is a simple implementation of a blockchain in Python. The goal is to understand the core mechanics of how blockchains work, including block structure, hashing, tampering detection, and a basic Proof-of-Work consensus mechanism.

## Table of Contents
- [Block Structure](#block-structure)
- [Validation Logic](#validation-logic)
- [Proof-of-Work Approach](#proof-of-work-approach)
- [How to Run the Project](#how-to-run-the-project)
- [License](#license)

## Block Structure

Each block in the blockchain consists of the following components:

- **Index**: The position of the block in the chain (starting from 0 for the genesis block).
- **Timestamp**: The time when the block was created.
- **Data**: The arbitrary payload (e.g., a string) that contains the information being stored.
- **Previous Hash**: The hash of the preceding block, linking the blocks together.
- **Hash**: A SHA-256 hash generated from the block's index, timestamp, data, previous hash, and nonce.
- **Nonce**: A number used in the Proof-of-Work process to find a valid hash.

## Validation Logic

The blockchain includes a method to validate its integrity:

- The `is_valid()` method checks:
  - Each block's hash is correctly calculated using the SHA-256 algorithm.
  - Each block's `previous_hash` matches the actual hash of its predecessor.
  
If any of these checks fail, the blockchain is considered invalid.

## Proof-of-Work Approach

To add a new block to the blockchain, a Proof-of-Work mechanism is implemented:

- Each block includes a nonce that is incremented until the block's hash meets a specific condition (e.g., starting with one leading zero).
- The `add_block(data)` method loops through nonce values, creating a new block and checking its hash until a valid nonce is found.
- This process ensures that adding blocks requires computational effort, enhancing the security of the blockchain.

## How to Run the Project

1. Ensure you have Python installed on your machine.
2. Clone this repository to your local machine.
3. Navigate to the directory containing the files.
4. Run the test script to see the blockchain in action:

   ```bash
   python test_blockchain.py
