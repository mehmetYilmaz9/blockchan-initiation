##genesis block (course section 3 :start with blockchain - 16 )
#BC is public ledfer of transaction
##basic example : implemented the blockchain and block data structures
from backend.blockchain.block import Block

class Blockchain : 
    """
    Blockchain : a public ledger of transactions.
    Implemented as a list of blocks - data sets of transactions
    """
    def __init__(self):
        self.chain = [Block.genesis()]

    def add_block(self, data): 
        self.chain.append(Block.mine_block(self.chain[-1], data))

    ##Python dunder methods 
    def __repr__(self):
        return f'Blockchain: {self.chain}'


def main():
    blockchain = Blockchain()
    blockchain.add_block('one')
    blockchain.add_block('two')

    print(blockchain)
    print(f'blockchain.py __name__: {__name__}')


if __name__ == '__main__':
    main()