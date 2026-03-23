from web3 import Web3

URL = "https://eth-mainnet.g.alchemy.com/v2/X3pY9VndnAbHRaCnF16ze"
w3 = Web3(Web3.HTTPProvider(URL))

# Mesmo bloco das questões anteriores
block = w3.eth.get_block(24722510)

print(f"Número do bloco:         {block.number}")
print(f"Proponente (miner):      {block['miner']}")
print(f"Hash do bloco:           {block['hash'].hex()}")
print(f"Nº de withdrawals:       {len(block.get('withdrawals', []))}")

# Lista os primeiros withdrawals (contêm índices de validadores)
print("\nValidadores (via withdrawals):")
for w in block.get("withdrawals", [])[:5]:
    print(f"  Índice do validador: {w['validatorIndex']} | Endereço: {w['address']}")
