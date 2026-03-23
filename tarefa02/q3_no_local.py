from web3 import Web3
import urllib.request
import json

# Conecta ao nó local via NiceNode
w3 = Web3(Web3.HTTPProvider("http://localhost:8545"))

print("=" * 55)
print("CONEXÃO")
print("=" * 55)
print(f"Conectado: {w3.is_connected()}")

if not w3.is_connected():
    print("Erro: nó local não está acessível em localhost:8545")
    exit()

# ─────────────────────────────────────────────
# QUESTÃO 2A — Bloco mais recente
# ─────────────────────────────────────────────
print("\n" + "=" * 55)
print("QUESTÃO 2A — Bloco mais recente")
print("=" * 55)

block = w3.eth.get_block("latest", full_transactions=True)
BLOCK_NUMBER = block.number

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

# ─────────────────────────────────────────────
# QUESTÃO 2B — Transação de maior valor
# ─────────────────────────────────────────────
print("\n" + "=" * 55)
print("QUESTÃO 2B — Transação de maior valor")
print("=" * 55)

if len(block.transactions) == 0:
    print("Bloco sem transações.")
else:
    maior_tx_valor = max(block.transactions, key=lambda tx: tx["value"])

    valor_wei = maior_tx_valor["value"]
    valor_eth = w3.from_wei(valor_wei, "ether")

    print(f"Hash da transação: {maior_tx_valor['hash'].hex()}")
    print(f"Origem  (from):    {maior_tx_valor['from']}")
    print(f"Destino (to):      {maior_tx_valor['to']}")
    print(f"Valor (Wei):       {valor_wei}")
    print(f"Valor (ETH):       {float(valor_eth):.8f}")

# ─────────────────────────────────────────────
# QUESTÃO 2C — Maior tarifa (gas * gasPrice)
# ─────────────────────────────────────────────
print("\n" + "=" * 55)
print("QUESTÃO 2C — Maior tarifa paga")
print("=" * 55)

if len(block.transactions) == 0:
    print("Bloco sem transações.")
else:
    maior_tx_tarifa = max(block.transactions, key=lambda tx: tx["gas"] * tx["gasPrice"])

    gas = maior_tx_tarifa["gas"]
    gas_price = maior_tx_tarifa["gasPrice"]
    tarifa_wei = gas * gas_price
    tarifa_eth = w3.from_wei(tarifa_wei, "ether")

    try:
        api = "https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=usd"
        with urllib.request.urlopen(api, timeout=5) as response:
            preco_eth_usd = json.loads(response.read())["ethereum"]["usd"]
        tarifa_usd = float(tarifa_eth) * preco_eth_usd
        usd_str = f"${tarifa_usd:.2f}"
        preco_str = f"${preco_eth_usd}"
    except:
        usd_str = "não disponível (sem acesso à API)"
        preco_str = "não disponível"

    print(f"Hash da transação:  {maior_tx_tarifa['hash'].hex()}")
    print(f"Gas (limite):       {gas}")
    print(f"Gas Price (Wei):    {gas_price}")
    print(f"Gas Price (Gwei):   {w3.from_wei(gas_price, 'gwei')}")
    print(f"Tarifa total (Wei): {tarifa_wei}")
    print(f"Tarifa total (ETH): {float(tarifa_eth):.8f}")
    print(f"Preço ETH (USD):    {preco_str}")
    print(f"Tarifa total (USD): {usd_str}")

# ─────────────────────────────────────────────
# QUESTÃO 2D — Proponente e validadores
# ─────────────────────────────────────────────
print("\n" + "=" * 55)
print("QUESTÃO 2D — Proponente e validadores")
print("=" * 55)

print(f"Número do bloco:         {block.number}")
print(f"Proponente (miner):      {block['miner']}")
print(f"Hash do bloco:           {block['hash'].hex()}")
print(f"Nº de withdrawals:       {len(block.get('withdrawals', []))}")

print("\nValidadores (via withdrawals):")
withdrawals = block.get("withdrawals", [])
if len(withdrawals) == 0:
    print("  Nenhum withdrawal neste bloco.")
else:
    for w in withdrawals[:5]:
        print(f"  Índice do validador: {w['validatorIndex']} | Endereço: {w['address']}")
