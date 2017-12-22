import hashlib
import datetime as date

class block:

    def __init__(self, index, timestamp, data, previousHash):
        self.index=index
        self.timestamp=timestamp
        self.data=data
        self.previousHash=previousHash
        self.hash = self.calculate_Hash()
        self.nonce = 0

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
            self.hash  = self.calculate_Hash()
            self.nonce += 1
        print "Mined Block: ", self.hash

class blockchain(block):

    def __init__(self):
        self.chain=[self.create_genesis_block()]
        self.difficulty = 1

    def create_genesis_block(self):
        return block(0, date.datetime.now(), "Genesis Block", "0")


    def get_latest_block(self):
        return self.chain[len(self.chain)-1]

    def add_block(self, new_block):
        new_block.previousHash = self.get_latest_block().hash
        #new_block.hash = new_block.calculate_Hash()
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def print_chain(self):
        for i in range(len(self.chain)):
            print "Block Num:",self.chain[i].index, "data:",self.chain[i].data
            print "Previous Hash:",self.chain[i].previousHash
            print "Current Hash",self.chain[i].calculate_Hash()

    def is_chain_valid(self):
        for i in range(1,len(self.chain)):
            if self.chain[i].hash != self.chain[i].calculate_Hash():
                return False
            elif self.chain[i-1].hash != self.chain[i].previousHash:
                return False
        return True


my_coin = blockchain()

print "Mining block 1..."
my_coin.add_block(block("1", "20/12/2017", 20, "0"))
print "Mining block 2..."
my_coin.add_block(block("2", "21/12/2017", 70, "0"))
print "Mining block 3..."
my_coin.add_block(block("3", "21/12/2017", 10, "0"))

my_coin.print_chain()
print my_coin.is_chain_valid()

my_coin.chain[2].data=100
my_coin.print_chain()
print my_coin.is_chain_valid()


