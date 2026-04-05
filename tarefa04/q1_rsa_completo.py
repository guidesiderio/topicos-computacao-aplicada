from sympy import mod_inverse

# ── Geração das chaves ──────────────────────────────────────
p, q = 61, 53
n = p * q
phi_n = (p - 1) * (q - 1)
e = 17
d = mod_inverse(e, phi_n)

print(f"=== Geração de chaves ===")
print(f"p={p}, q={q}, n={n}, φ(n)={phi_n}")
print(f"Chave pública:  (e={e}, n={n})")
print(f"Chave privada:  (d={d}, n={n})\n")

# ── Cifrando com chave privada (assinatura) ──────────────────
mensagem = "VIVA"
print(f"=== Cifrando '{mensagem}' com chave privada ===")
cifra = []
for letra in mensagem:
    m = ord(letra)
    c = pow(m, d, n)
    cifra.append(c)
    print(f"  {letra} (m={m}) → C={c}")

print(f"Cifra: {cifra}\n")

# ── Verificando com chave pública ────────────────────────────
print(f"=== Verificando cifra com chave pública ===")
verificado = ""
for c in cifra:
    m = pow(c, e, n)
    verificado += chr(m)
    print(f"  C={c} → m={m} → '{chr(m)}'")

print(f"Mensagem verificada: {verificado}")
