from web3 import Web3
from eth_account import Account

# ── Configuração ─────────────────────────────────────────────
ALCHEMY_URL = "https://eth-sepolia.g.alchemy.com/v2/SUA_CHAVE"
w3 = Web3(Web3.HTTPProvider(ALCHEMY_URL))

# Conta criada na Questão 2
CHAVE_PRIVADA = "0xSUA_CHAVE_PRIVADA"
conta = Account.from_key(CHAVE_PRIVADA)
endereco_from = conta.address

# Endereço do professor (destino)
endereco_to = "0x2E943a50311626d80DD1848Dc965BC814d014e90"

print(f"Remetente:      {endereco_from}")
print(f"Destinatário:   {endereco_to}")
print(f"Rede:           Sepolia (chain_id=11155111)")
print(f"Conectado:      {w3.is_connected()}")

# ── Etapa 1: Construção da transação ─────────────────────────
valor_eth = 0.05  # quantidade enviada
valor_wei = w3.to_wei(valor_eth, "ether")

nonce = w3.eth.get_transaction_count(endereco_from)
gas_price = w3.eth.gas_price
gas_limit = 21000  # tx simples (sem contrato)

transacao = {
    "nonce": nonce,
    "to": endereco_to,
    "value": valor_wei,
    "gas": gas_limit,
    "gasPrice": gas_price,
    "chainId": 11155111,  # Sepolia chain ID
}

print(f"\n=== Transação construída ===")
print(f"Nonce:          {nonce}")
print(f"Valor:          {valor_eth} ETH ({valor_wei} Wei)")
print(f"Gas limit:      {gas_limit}")
print(f"Gas price:      {w3.from_wei(gas_price, 'gwei'):.4f} Gwei")

# ── Etapa 2: Assinatura com chave privada (autenticação) ─────
tx_assinada = w3.eth.account.sign_transaction(transacao, CHAVE_PRIVADA)

print(f"\n=== Assinatura ECDSA ===")
print(f"v:  {tx_assinada.v}")
print(f"r:  {hex(tx_assinada.r)}")
print(f"s:  {hex(tx_assinada.s)}")
print(f"Hash da tx:     {tx_assinada.hash.hex()}")

# ── Etapa 3: Envio à rede ────────────────────────────────────
tx_hash = w3.eth.send_raw_transaction(tx_assinada.raw_transaction)

print(f"\n=== Transação enviada ===")
print(f"TX Hash:  0x{tx_hash.hex()}")
print(f"Acompanhe em: https://sepolia.etherscan.io/tx/0x{tx_hash.hex()}")

# ── Aguarda confirmação ───────────────────────────────────────
recibo = w3.eth.wait_for_transaction_receipt(tx_hash)

print(f"\n=== Recibo da transação ===")
print(f"Status:         {'Sucesso' if recibo.status == 1 else 'Falhou'}")
print(f"Bloco:          {recibo.blockNumber}")
print(f"Gas usado:      {recibo.gasUsed}")
