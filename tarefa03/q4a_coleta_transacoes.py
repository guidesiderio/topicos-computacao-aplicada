from web3 import Web3
import pandas as pd
import time
from dotenv import load_dotenv
import os

load_dotenv()

URL = f"https://eth-mainnet.g.alchemy.com/v2/{os.getenv('ALCHEMY_API_KEY')}"
w3 = Web3(Web3.HTTPProvider(URL))

finalized_block = w3.eth.get_block("finalized")
start_block = finalized_block.number

transactions = []
block_num = start_block
blocks_visitados = set()

print(f"Bloco finalizado mais recente: {start_block}")
print("Coletando transações...")

while len(transactions) < 40:
    if block_num in blocks_visitados:
        block_num -= 1
        continue

    try:
        block = w3.eth.get_block(block_num, full_transactions=True)
        blocks_visitados.add(block_num)

        base_fee = block.get("baseFeePerGas", 0)

        if block.transactions:
            tx = block.transactions[0]

            gas_price = tx.get("gasPrice", 0)
            max_fee = tx.get("maxFeePerGas", None)
            max_priority = tx.get("maxPriorityFeePerGas", None)

            transactions.append(
                {
                    "hash": tx["hash"].hex(),
                    "block_number": block_num,
                    "base_fee_wei": base_fee,
                    "max_fee_wei": max_fee,
                    "max_priority_fee_wei": max_priority,
                    "gas_limit": tx["gas"],
                    "gas_price_wei": gas_price,
                }
            )

        print(
            f"Bloco {block_num}: {len(block.transactions)} txs | Total coletado: {len(transactions)}"
        )
        block_num -= 1
        time.sleep(0.3)

    except Exception as e:
        print(f"Erro no bloco {block_num}: {e}")
        block_num -= 1

df = pd.DataFrame(transactions)
df.to_csv("transacoes_finalizadas.csv", index=False)
print(f"\nCSV salvo com {len(df)} transações de {len(blocks_visitados)} blocos distintos.")
print(df[["hash", "base_fee_wei", "max_fee_wei", "gas_price_wei"]].head())
