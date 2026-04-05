from web3 import Web3
import pandas as pd
import time
from dotenv import load_dotenv
import os

load_dotenv()

URL = f"https://eth-mainnet.g.alchemy.com/v2/{os.getenv('ALCHEMY_API_KEY')}"
w3 = Web3(Web3.HTTPProvider(URL))

pendentes = []
hashes_vistos = set()

print("Coletando transações pendentes da mempool...")

while len(pendentes) < 40:
    try:
        # Pega bloco pendente
        block = w3.eth.get_block("pending", full_transactions=True)

        for tx in block.transactions:
            h = tx["hash"].hex()
            if h in hashes_vistos:
                continue
            hashes_vistos.add(h)

            pendentes.append(
                {
                    "hash": h,
                    "max_fee_wei": tx.get("maxFeePerGas", None),
                    "max_priority_fee_wei": tx.get("maxPriorityFeePerGas", None),
                    "gas_limit": tx.get("gas", None),
                    "gas_price_wei": tx.get("gasPrice", None),
                }
            )

            if len(pendentes) >= 40:
                break

        print(f"Coletados: {len(pendentes)}/40")
        time.sleep(2)

    except Exception as e:
        print(f"Erro: {e}")
        time.sleep(2)

df = pd.DataFrame(pendentes)
df.to_csv("transacoes_pendentes.csv", index=False)
print(f"\nCSV salvo com {len(df)} transações pendentes.")
print(df[["hash", "max_fee_wei", "max_priority_fee_wei", "gas_limit"]].head())
