import pandas as pd

df = pd.read_csv("transacoes_finalizadas.csv")

df_eip1559 = df[df["max_fee_wei"].notna()].copy()

usou_max_fee = df_eip1559[df_eip1559["gas_price_wei"] >= df_eip1559["max_fee_wei"]]

total = len(df_eip1559)
count = len(usou_max_fee)

print(f"Transações EIP-1559 analisadas: {total}")
print(f"Transações que usaram o max fee: {count}")
print(f"Porcentagem: {(count / total) * 100:.2f}%")

if count > 0:
    print("\nExemplos:")
    print(usou_max_fee[["hash", "max_fee_wei", "gas_price_wei"]].head())
