import hashlib

class block:
    def __init__(self, index, timestamp, data, previousHash):
        self.index=index
        self.timestamp=timestamp
        self.data=data
        self.previousHash=previousHash
        self.hash = ''

    def calculate_Hash():
        return str(hashlib.sha256(self.index + self.timestamp + self.previousHash + str(self.data)))

class blockchain:
    def __init__(self):
        self.chain=[]

    def create_genesis_block():
        return block(0,str(now),"Genesis Block", 0)
