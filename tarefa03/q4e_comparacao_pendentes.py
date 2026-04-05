import pandas as pd

df_fin = pd.read_csv("transacoes_finalizadas.csv")
df_pend = pd.read_csv("transacoes_pendentes.csv")

campos = ["max_fee_wei", "max_priority_fee_wei", "gas_limit", "gas_price_wei"]
campos_pend = ["max_fee_wei", "max_priority_fee_wei", "gas_limit"]

print("=== Transações FINALIZADAS ===")
for col in campos:
    if col in df_fin.columns:
        vals = df_fin[col].dropna()
        print(f"{col}:")
        print(f"  Média:   {vals.mean():.0f}")
        print(f"  Mediana: {vals.median():.0f}")

print("\n=== Transações PENDENTES ===")
for col in campos_pend:
    if col in df_pend.columns:
        vals = df_pend[col].dropna()
        print(f"{col}:")
        print(f"  Média:   {vals.mean():.0f}")
        print(f"  Mediana: {vals.median():.0f}")
