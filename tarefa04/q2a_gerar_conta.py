from eth_account import Account
import secrets

# Gera 32 bytes aleatórios seguros → chave privada
chave_privada = "0x" + secrets.token_hex(32)

# Deriva a conta (chave pública + endereço) a partir da privada
conta = Account.from_key(chave_privada)

print(f"Chave privada:  {chave_privada}")
print(f"Chave pública:  {conta._key_obj.public_key}")
print(f"Endereço EOA:   {conta.address}")
