# NODE # 
# $ERVER$Y$TEM # 
# BLOCKCHAIN #

import datetime
import hashlib as hasher

#==============================================================================================#
class Genesis_Block:
    '''
    In the begining there was light.
    The genesis block is the begining of any data flow through the branching-blockchain system.
    This block is the begining and contains the anchor hash for the proceding block.
    Every chain begins with a Genesis_block object. 
    '''

    def __init__(self, data):
        self.index = 0
        self.genesis_data = data
        self.timestamp = self.__timestamp()
        self.current_hash = self.__current_hash()
    
    def __timestamp(self):
        return datetime.datetime.now()

    def __current_hash(self):
        sha = hasher.sha256()
        sha.update(str(self.index).encode('utf-8') + 
                   str(self.timestamp).encode('utf-8') + 
                   str(self.genesis_data).encode('utf-8'))
        return sha.hexdigest()

#==============================================================================================#
class Block:
    '''
    Block is the very highest abstraction in the branching blockchain model.
    The previous and current hash are required args to instantiate a Block object.
    A block object references the next hash in the sequence.
    '''

    def __init__(self, previoushash, currenthash):
        self.previous_hash = previoushash
        self.current_hash = currenthash
        self.next_hash = self.next_bhash()

    def next_bhash(self):
        shha = hasher.sha256()
        shha.update(str(self.previous_hash).encode('utf-8') +
                    str(self.current_hash).encode('utf-8'))
        return shha.hexdigest()

#==============================================================================================#
class Blockchain:
    '''
    # BLOCKCHAIN
    # Stores current blockchain information and chain functions
    # All storage is dynamic and is determined by the users actions
    '''
    def __init__(self):
        self.chain = []
        self.current_transactions = 0
        self.genesis_block = self.generate_genesis_block()


    def start_chain(self):
        self.chain.append(self.genesis_block)
        self.check = self.current_transactions + self.genesis_block.index
        if self.check == 0:
            self.new_block()

    def generate_genesis_block(self):
        self.gb = Genesis_Block('genesis')
        return self.gb

    def new_block(self):
        # pipe in the next nodes block data
        self.__block = self.__pipe_4_block()
        
        return self.__block
    
    def __pipe_4_block(self):
        return True

    @property
    def current_block(self):
        return True

    @property
    def last_block(self):
        return True
        

