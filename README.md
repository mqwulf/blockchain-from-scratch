## Blockchain from scratch
Basic blockchain program made from scratch with simple functionalities to add transactions (blocks) and verification of the chain. It demonstrates how a blockchain can be used to maintain a sequence of transactions and ensure their validity through hashing.


## Features
- **Sequential block addition**
- **Hash-based linkage between blocks**
- **Integrity verification through hash comparison**

## Hashing Attributes
- **data: Contains the transaction or data for the block**
- **prev_hash: Holds the hash of the previous block, creating a link between blocks**
- **hash: A unique hash generated from the current block's data and the previous block's hash, ensuring data integrity**
- **next: A pointer to the next block in the chain**

```python
Transaction added.   New hash is -818999441925753433
Transaction added.   New hash is 1389406566138283050
Transaction added.   New hash is 6515321633647078780
Transaction added.   New hash is -3837324993158193350

Replaying Blockchain 
Starting Balance Eric = $1000
Eric Pays Spongebob $10 for providing a great idea
Eric Pays the cat $50 for ending the noise
The cat pays Pet Food Express $20 for catnip
Blockchain Verified. End of Transactions
Final hash is -3837324993158193350

Replaying Blockchain 
Starting Balance Eric = $1000
Eric Pays Spongebob $10 for providing a great idea
Blockchain is Corrupted!!
```
