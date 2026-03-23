from web3 import Web3

# Substitua pela sua chave do Alchemy
URL = "https://eth-mainnet.g.alchemy.com/v2/X3pY9VndnAbHRaCnF16ze"
w3 = Web3(Web3.HTTPProvider(URL))

# Verifica conexão
print("Conectado:", w3.is_connected())

# Obtém o bloco mais recente com todas as transações
block = w3.eth.get_block("latest", full_transactions=True)

# Verifica se é finalizado
try:
    finalized_block = w3.eth.get_block("finalized")
    is_finalized = block.number <= finalized_block.number
except:
    is_finalized = "não disponível"

print(f"Número do bloco:       {block.number}")
print(f"Bloco finalizado:      {is_finalized}")
print(f"Nº de transações:      {len(block.transactions)}")
print(f"Gas usado (gasUsed):   {block.gasUsed}")
print(f"Gas limite (gasLimit): {block.gasLimit}")
print(f"Uso do bloco:          {round(block.gasUsed / block.gasLimit * 100, 2)}%")
