from web3 import Web3
import urllib.request
import json

URL = "https://eth-mainnet.g.alchemy.com/v2/X3pY9VndnAbHRaCnF16ze"
w3 = Web3(Web3.HTTPProvider(URL))

# Mesmo bloco das questões anteriores
block = w3.eth.get_block(24722510, full_transactions=True)

# Calcula a tarifa de cada transação: gas * gasPrice
maior_tx = max(block.transactions, key=lambda tx: tx["gas"] * tx["gasPrice"])

gas = maior_tx["gas"]
gas_price = maior_tx["gasPrice"]
tarifa_wei = gas * gas_price
tarifa_eth = w3.from_wei(tarifa_wei, "ether")

# Busca preço atual do ETH em USD via CoinGecko
api = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
with urllib.request.urlopen(api) as response:
    preco_eth_usd = json.loads(response.read())["ethereum"]["usd"]

tarifa_usd = float(tarifa_eth) * preco_eth_usd

print(f"Hash da transação:  {maior_tx['hash'].hex()}")
print(f"Gas (limite):       {gas}")
print(f"Gas Price (Wei):    {gas_price}")
print(f"Gas Price (Gwei):   {w3.from_wei(gas_price, 'gwei')}")
print(f"Tarifa total (Wei): {tarifa_wei}")
print(f"Tarifa total (ETH): {float(tarifa_eth):.8f}")
print(f"Preço ETH (USD):    ${preco_eth_usd}")
print(f"Tarifa total (USD): ${tarifa_usd:.2f}")
