from web3 import Web3

private_key = ""
receiver_address = ""
message = b""


NODE_URL = 'https://rpc.sepolia.org' # Sepolia node
CHAIN_ID = 11155111 # Sepolia network id
# connect to Sepolia
w3 = Web3(Web3.HTTPProvider(NODE_URL))
if not w3.is_connected():
    raise Exception("Connect to Sepolia network failed.")

sender = w3.eth.account.from_key(private_key)

# transaction params
transaction_params = {
'from': sender.address,
'to': receiver_address, # todo:receiver address
'value': w3.to_wei(0.001, 'ether'), # todo:fee
'data': message, # todo:additional message
'nonce': w3.eth.get_transaction_count(sender.address), # todo:nonce
'chainId': CHAIN_ID # network id
}
nonce = w3.eth.estimate_gas(transaction_params)

gas_estimate = w3.eth.estimate_gas(transaction_params)
gas_price = w3.eth.gas_price
transaction_params.update({
    'gas': gas_estimate,
    'gasPrice': gas_price + w3.to_wei(2, 'gwei')
})

# update transaction params
transaction_params.update({
'gas': gas_estimate, # todo:estimated gas
'gasPrice': gas_price # todo:gas price
})

# Send transaction by private key
signed_txn = w3.eth.account.sign_transaction(transaction_params, sender._private_key)

# Process transaction
txn_hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

print(f'Transaction sent with hash: {txn_hash.hex()}')