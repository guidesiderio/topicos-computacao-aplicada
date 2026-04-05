import pandas as pd

df = pd.read_csv("transacoes_finalizadas.csv")

df = df[df["gas_price_wei"] > 0].copy()

df["pct_base_fee"] = (df["base_fee_wei"] / df["gas_price_wei"]) * 100

print("=== Porcentagem que a base fee representa do gas price ===\n")
print(f"Média:   {df['pct_base_fee'].mean():.2f}%")
print(f"Mínimo:  {df['pct_base_fee'].min():.2f}%")
print(f"Mediana: {df['pct_base_fee'].median():.2f}%")
print(f"Máximo:  {df['pct_base_fee'].max():.2f}%")

df[["hash", "base_fee_wei", "gas_price_wei", "pct_base_fee"]].to_csv(
    "transacoes_com_pct.csv", index=False
)
print("\nCSV com percentuais salvo em transacoes_com_pct.csv")
