from datetime import datetime
from hashlib import sha256
import json


class Blockchain(object):
    def __init__(self) -> None:
        self.chain = []
        self.pending_transactions = []
        
        # Create the genesis block
        print("Creating genesis block")
        self.new_block()
        
    def new_block(self, previous_hash=None):
        # Generates a new block and add it to the chain
        block = {
            'index': len(self.chain),
            'timestamp': datetime.utcnow().isoformat(),
            'transactions': self.pending_transactions,
            'previous_hash': previous_hash
        }
        # Get the hash of this new block, and add it to the above block
        block_hash = self.hash(block)
        block["hash"] = block_hash
        
        # Reset the list of pending transactions
        self.pending_transactions = []
        # Add the block to chain
        self.chain.append(block)
        
        print(f"Created block{block['index']}")
        return block
        
        
    @staticmethod
    def hash(block):
        # Hashes a Block
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()
        
    
    def last_block(self):
        # Gets the latest block in the chain
        return self.chain[-1] if self.chain else None
    
    def new_transaction(self, sender, recipinent, amount):
        # Adds a new transaction to the list of pending transactions
        self.pending_transactions.append({
            "recipinent": recipinent,
            "sender": sender,
            "amount": amount
        })
    