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
    
    def register_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)
    
    def valid_chain(self, chain):
        last_block = chain[0]
        current_index = 1
        while current_index < len(chain):
            block = chain[current_index]
            if block['previous_hash'] != self.hash(last_block):
                return False
            # Check that the Proof of Work is correct
            if not self.valid_proof(last_block['proof'], block['proof']):
                return False
            last_block = block
            current_index += 1
        return True

    def resolve_conflicts(self):
        neighbours = self.nodes
        new_chain = None
        max_length = len(self.chain)
        for node in neighbours:
            response = requests.get('http://%s/chain' %node)
            if response.status_code == 200:
                length = json.loads(response)['length']
                chain = json.loads(response)['chain']
            # Check if the length is longer and the chain is valid
            if length > max_length and self.valid_chain(chain):
                max_length = length
                new_chain = chain
        # Replace our chain if we discovered a new, valid chain longer than ours
        if new_chain:
            self.chain = new_chain
            return True
        return False
        
        
        
        
        
        
node_identifier = str(uuid4()).replace('-', '')
# Instantiate the Blockchain
blockchain = Blockchain()

def mine(request):
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)
    print(proof)
    blockchain.new_transaction(
         sender="0",
         recipient=node_identifier,
         amount=1,
    )
    # Forge the new Block by adding it to the chain
    block = blockchain.new_block(proof)
    response = {
     'message': "New Block Forged",
     'index': block['index'],
     'transactions': block['transactions'],
     'proof': block['proof'],
     'previous_hash': block['previous_hash'],
    }
    print(response)
    return HttpResponse(json.dumps(response))
    
def new_transaction(request):
    values = json.loads(request.body.decode('utf-8'))
    required = ['sender', 'recipient', 'amount']
    if not all(k in values for k in required):
    return 'Missing values'
    index = blockchain.new_transaction(values['sender'], values['recipient'], values['amount'])
    print(index)
    response = {'message': 'Transaction will be added to Block %s'%index}
    return HttpResponse(json.dumps(response))
    
def full_chain(request):
    response = {
    'chain': blockchain.chain,
    'length': len(blockchain.chain),
    }
    return HttpResponse(json.dumps(response))

def register_node(self, address):
    parsed_url = urlparse(address)
    self.nodes.add(parsed_url.netloc)

