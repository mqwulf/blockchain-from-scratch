class Block:
    def __init__(self, data, prev_hash=0):
        self._data = data
        self._prev_hash = prev_hash
        self._hash = hash((self._data, self._prev_hash))
        self._next = None
        print(f"Transaction added.   New hash is {self._hash}")
    def add_block(self, data):
        curr = self
        while curr._next:
            curr = curr._next
        newblock = Block(data, curr._hash)
        curr._next = newblock

    def replay(self, prev_hash=0):
        curr = self
        print("Replaying Blockchain ")
        while curr is not None:
            if curr._hash != hash((curr._data, prev_hash)):
                print("Blockchain is Corrupted!!")
                return
            print(curr._data)
            prev_hash = curr._hash
            curr = curr._next
        print("Blockchain Verified. End of Transactions")
        print(f"Final hash is {prev_hash}")


new_chain = Block("Starting Balance Eric = $1000")
new_chain.add_block("Eric Pays Spongebob $10 for providing a great idea")
new_chain.add_block("Eric Pays the cat $50 for ending the noise")
new_chain.add_block("The cat pays Pet Food Express $20 for catnip")
print()
new_chain.replay()
print()

# Cat tried to hack the chain
fraud = "Eric Pays the cat $500 for ending the noise"
new_chain._next._next._data = fraud
new_chain.replay()