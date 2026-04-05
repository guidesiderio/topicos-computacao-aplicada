from eth_account import Account
from eth_keys import keys
from Crypto.Hash import keccak
import secrets

# ── Geração da chave privada ─────────────────────────────────
chave_privada_hex = secrets.token_hex(32)
chave_privada_bytes = bytes.fromhex(chave_privada_hex)

print(f"Chave privada:  0x{chave_privada_hex}")

# ── Derivação da chave pública (ponto na curva secp256k1) ────
private_key_obj = keys.PrivateKey(chave_privada_bytes)
chave_publica = private_key_obj.public_key
chave_publica_bytes = bytes(chave_publica)  # 64 bytes (sem prefixo 0x04)

print(f"Chave pública:  0x04{chave_publica_bytes.hex()}")
print(f"  → x: {chave_publica_bytes[:32].hex()}")
print(f"  → y: {chave_publica_bytes[32:].hex()}")

# ── Keccak-256 sobre a chave pública ─────────────────────────
k = keccak.new(digest_bits=256)
k.update(chave_publica_bytes)
hash_keccak = k.hexdigest()

print(f"\nKeccak-256 da chave pública:")
print(f"  {hash_keccak}  (32 bytes)")

# ── Endereço = últimos 20 bytes do hash ──────────────────────
endereco = "0x" + hash_keccak[-40:]

print(f"\nEndereço EOA (últimos 20 bytes):")
print(f"  {endereco}")

# ── Verificação com eth_account ───────────────────────────────
conta = Account.from_key("0x" + chave_privada_hex)
print(f"\nVerificação via eth_account:")
print(f"  {conta.address}")
print(f"  Corresponde: {conta.address.lower() == endereco.lower()}")
