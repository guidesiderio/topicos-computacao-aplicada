from web3 import Web3
from eth_account._utils.signing import sign_transaction_dict
from eth_account import Account

ALCHEMY_URL = "https://eth-sepolia.g.alchemy.com/v2/SUA_CHAVE"
w3 = Web3(Web3.HTTPProvider(ALCHEMY_URL))

# Hash da transação enviada no item (a)
TX_HASH = "0xSEU_TX_HASH_AQUI"

# ── Busca a transação na rede ────────────────────────────────
tx = w3.eth.get_transaction(TX_HASH)

print(f"=== Dados da transação ===")
print(f"From (endereço): {tx['from']}")
print(f"v: {tx['v']}")
print(f"r: {hex(tx['r'])}")
print(f"s: {hex(tx['s'])}")

# ── Recuperação da chave pública via eth_account ─────────────
# Reconstrói os campos da transação para montar o hash assinado
tx_dados = {
    "nonce": tx["nonce"],
    "gasPrice": tx["gasPrice"],
    "gas": tx["gas"],
    "to": tx["to"],
    "value": tx["value"],
    "data": tx["input"],
    "chainId": 11155111,
}

# Recupera o endereço do signatário a partir da assinatura
signatario = Account.recover_transaction(tx_dados, vrs=(tx["v"], tx["r"], tx["s"]))

print(f"\n=== Recuperação da chave pública ===")
print(f"Endereço recuperado:  {signatario}")
print(f"Endereço original:    {tx['from']}")
print(f"Autenticação válida:  {signatario.lower() == tx['from'].lower()}")
