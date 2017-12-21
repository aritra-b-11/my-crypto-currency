import hashlib
import datetime as date

class block:
    def __init__(self, index, timestamp, data, previousHash):
        self.index=index
        self.timestamp=timestamp
        self.data=data
        self.previousHash=previousHash
        self.hash = self.calculate_Hash()

    def calculate_Hash(self):
        sha = hashlib.sha256()
        sha.update(
            str(self.index)+
            str(self.timestamp)+
            str(self.data)+
            str(self.previousHash))
        #        return str(hashlib.sha256(self.index + self.timestamp + self.previousHash + str(self.data)))
        return sha.hexdigest()

    def return_prev_hash(self):
        return str(self.previousHash)


class blockchain:

    def __init__(self):
        self.chain=[self.create_genesis_block()]

    def create_genesis_block(self):
        return block(0, date.datetime.now(), "Genesis Block", "0")


    def get_latest_block(self):
        return self.chain[len(self.chain)-1]

    def add_block(self, new_block):
        new_block.previousHash = self.get_latest_block().hash
        new_block.hash = new_block.calculate_Hash()
        self.chain.append(new_block)



my_coin = blockchain()

my_block =  my_coin.get_latest_block()
print "prev",my_block.return_prev_hash()
print "current",my_block.calculate_Hash()

my_coin.add_block(block("1", "20/12/2017", 20, "0"))
my_block =  my_coin.get_latest_block()
print "prev",my_block.return_prev_hash()
print "current",my_block.calculate_Hash()

my_coin.add_block(block("2", "21/12/2017", 70, "0"))
my_block =  my_coin.get_latest_block()
print "prev",my_block.return_prev_hash()
print "current",my_block.calculate_Hash()



