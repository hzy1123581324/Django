from django.shortcuts import render
import hashlib
import json
from time import time
from uuid import uuid4
# Create your views here.


'''
块结构
block = {
  'index': 1,
  'timestamp': 1506057125.900785,
  'transactions': [
    {
      'sender': "8527147fe1f5426f9dd545de4b27ee00",
      'recipient': "a77f5cdfa2934df3954a5c7c7da5df1f",
      'amount': 5,
    }
  ],
  'proof': 324984774000,
  'previous_hash': "2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824"
}
'''

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash=1, proof=100)
        self.nodes = set()
   
    
    def new_block(self,proof,previous_hash= None):
        # Creates a new Block and adds it to the chain
        block = {
          'index': len(self.chain) + 1,
          'timestamp': time(),
          'transactions': self.current_transactions,
          'proof':proof ,
          'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
        self.chain.append(block)
        return block
    
    def new_transaction(self):
        # Adds a new transaction to the list of transactions
        """
        生成新交易信息，信息将加入到下一个待挖的区块中
        :param sender: <str> Address of the Sender
        :param recipient: <str> Address of the Recipient
        :param amount: <int> Amount
        :return: <int> The index of the Block that will hold this transaction
        """
        self.current_transactions.append({
          'sender': sender,
          'recipient': recipient,
          'amount': amount,
        })
        return self.last_block['index'] + 1
    
    @staticmethod
    def hash(block):
        # Hashes a Block
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()


    @property
    def last_block(self):
        # Returns the last Block in the chain
        return self.chain[-1]
    

        
    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
          proof += 1
        return proof
        
    @staticmethod
    def valid_proof(last_proof, proof):
        guess = str(last_proof*proof).encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:5] == "00000"


