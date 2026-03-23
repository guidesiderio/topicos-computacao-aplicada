from web3 import Web3

URL = "https://eth-mainnet.g.alchemy.com/v2/X3pY9VndnAbHRaCnF16ze"
w3 = Web3(Web3.HTTPProvider(URL))

# Usa o mesmo bloco da questão anterior
block = w3.eth.get_block(24722510, full_transactions=True)

# Encontra a transação de maior valor
maior_tx = max(block.transactions, key=lambda tx: tx["value"])

valor_wei = maior_tx["value"]
valor_eth = w3.from_wei(valor_wei, "ether")

print(f"Hash da transação: {maior_tx['hash'].hex()}")
print(f"Origem  (from):    {maior_tx['from']}")
print(f"Destino (to):      {maior_tx['to']}")
print(f"Valor (Wei):       {valor_wei}")
print(f"Valor (ETH):       {valor_eth}")
