from web3 import Web3
import os
import json

NODE_URL = 'https://rpc.sepolia.org' # Sepolia node
CHAIN_ID = 11155111 # Sepolia network id
# connect to Sepolia
w3 = Web3(Web3.HTTPProvider(NODE_URL))
if not w3.is_connected():
    raise Exception("Connect to Sepolia network failed.")

if not os.path.isfile('key.json'):
# Create new account
    account = w3.eth.account.create()
    public_key = str(account._key_obj.public_key)
    private_key = account.key.hex()
    new_address = account.address
    account_profile = {
    'address': new_address,
    'private_key': private_key,
    'public_key': public_key}
# Save the account
    with open('key.json', 'w') as f:
        json.dump(account_profile, f)
else:
# Load the account
    with open('key.json', 'r') as f:
        account_profile = json.load(f)

