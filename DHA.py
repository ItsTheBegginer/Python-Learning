p = 31
g = 3

alice_private = int(input("Enter private key for alice:"))

bob_private = int(input("Enter private key for bob:"))

bob_public = pow(g,bob_private,p)
alice_public = pow(g,alice_private,p)


shared_bob = pow(alice_public,bob_private,p)
shared_alice = pow(bob_public,alice_private,p)

print(f"\nPublic parameters: p={p}, g={g}")
print(f"Alice Private Key: {alice_private}, Public Key: {alice_public}")
print(f"Bob Private Key: {bob_private}, Public Key: {bob_public}")
print(f"Shared Secret: {shared_alice}")