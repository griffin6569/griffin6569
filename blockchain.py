import hashlib

blockchain = []

def record_transaction(start, destination, route):
    transaction = f"{start} -> {destination}: {route}"
    block_hash = hashlib.sha256(transaction.encode()).hexdigest()
    blockchain.append(block_hash)
    print("✅ Transaction Secured:", block_hash)
