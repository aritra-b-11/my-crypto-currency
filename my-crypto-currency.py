"""
Starting the blockchain code.

We need :
1. hash lib for the hashing algorithm.
2. date time for capturing the current date.
"""


import hashlib
import datetime as date

"""
We will start with the defination of the block:
a Block sould take input as :
1. index
2. timestamp
3. data
4. previous hash

from this we will calculate the hash of this block. For calculating
the hash we will need nonce=number used only once"""

class block:

    def __init__(self, index, timestamp, data, previousHash):
        self.index=index
        self.timestamp=timestamp
        self.data=data
        self.previousHash=previousHash
        self.nonce = 0
        self.hash = self.calculate_Hash()


        # lets define the calculate hash function. I am using sha1

    def calculate_Hash(self):
        sha = hashlib.sha1()
        sha.update(
            str(self.index) +
            str(self.timestamp) +
            str(self.data) +
            str(self.previousHash) +
            str(self.nonce)
        )
        return sha.hexdigest()



    def mine_block(self,difficulty):
        while(self.hash[:difficulty] != "0"*difficulty):
            self.hash = self.calculate_Hash()
            self.nonce += 1
        print "Mined Block: ", self.hash
        return self.hash

    def check_if_mined(self,difficulty):
        new_hash= ""
        self.nonce=0
        while(new_hash[:difficulty] != "0"*difficulty):
            new_hash = self.calculate_Hash()
            self.nonce +=1
        return new_hash


""" The class blockchain is defined from here.

Now class blockchain is a subclass of block. So we can inherit the
class block property to it."""

class blockchain(block):

    def __init__(self):
        # this is the chain def
        self.chain=[self.create_genesis_block()]
        # difficulty will be needed for mining.
        self.difficulty = 3


    #first block needs to be the Genesis Block

    def create_genesis_block(self):
        return block(0, date.datetime.now(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[len(self.chain)-1]

    def add_block(self, new_block):
        new_block.previousHash = self.get_latest_block().hash
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def print_chain(self):
        print "Starting Blockchain:"
        print "Block Num:",self.chain[0].index,"data:",self.chain[0].data
        print "previous Hash:",self.chain[0].previousHash
        print "current Hash",self.chain[0].calculate_Hash()
        for i in range(1,len(self.chain)):
            print "Block Num:",self.chain[i].index, "data:",self.chain[i].data
            print "Previous Hash:",self.chain[i].previousHash
            print "Current Hash",self.chain[i].mine_block(self.difficulty)

    def is_chain_valid(self):
        for i in range(1,len(self.chain)):
            if self.chain[i].hash != self.chain[i].check_if_mined(self.difficulty):
                print "current hash", self.chain[i].hash," do not match with mined hash",self.chain[i].check_if_mined(self.difficulty)
                return False
            elif self.chain[i-1].hash != self.chain[i].previousHash:
                print "previous hash",self.chain[i-1].hash," does not match with attribute prev Hash",self.chain[i].previousHash
                return False
        return True



# thats all about blockchain def. Next part is for testing the chain.

my_coin = blockchain()

print "Mining block 1..."
my_coin.add_block(block("1", "20/12/2017", 20, "0"))
print "Mining block 2..."
my_coin.add_block(block("2", "21/12/2017", 70, "0"))
print "Mining block 3..."
my_coin.add_block(block("3", "21/12/2017", 10, "0"))
print "----------------------"
my_coin.print_chain()
print "----------------------"
print my_coin.is_chain_valid()
print "----------------------"

my_coin.chain[2].data=100
my_coin.print_chain()
print my_coin.is_chain_valid()
print "----------------------"

