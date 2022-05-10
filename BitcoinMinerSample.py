# -*- coding: utf-8 -*-
"""
Simple Blockchain Miner 
Proof of Concept
Arindam Misra, TPRU, Department of Revenue
"""
from timeit import default_timer as timer
import hashlib # Import the Hashing library in Python
MAX_NONCE=1000000000000
num_zeros=6
#Sample Hash function
tx_t="Sample Bitcoin Hasher."
print("The SHA256 Hash of \"",tx_t,"\"is:")
print(hashlib.sha256(tx_t.encode()).hexdigest())

def sampleminer(block_no,trstring,prev_hash):
    for i in range(MAX_NONCE):
        full_block=str(block_no)+trstring+ prev_hash+str(i)
        curr_itr_hash=hashlib.sha256(full_block.encode()).hexdigest()
        if curr_itr_hash.startswith('0'*num_zeros):
            print(f"The Nonce: {i} produces SHA256 hash with ",num_zeros," zeros. Hence block solved\n")
            print("The Hash is : ",curr_itr_hash,"\n")
            return curr_itr_hash
    return -1

blockno=56
transactionstring = """
Prev hash=62079f5c3554d1fb1988d6001d2fcbeb4dbc517df4387bb84df15207a3ac2f60
Std Reward 6.5 
User Reward 1.445 
Give A 23 
Give B 16 
Give C 59 
Give D 34
Nonce
"""
previoushash="62079f5c3554d1fb1988d6001d2fcbeb4dbc517df4387bb84df15207a3ac2f60"
start = timer()
sampleminer(blockno,transactionstring,previoushash)
end = timer()
print("\n Time taken for ",num_zeros," zeros is :",end-start,"seconds\n")
    
