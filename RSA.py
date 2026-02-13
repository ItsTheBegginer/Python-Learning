import base64
from math import gcd

p, q = 17, 23
n = p * q
phi = (p - 1) * (q - 1)

e = 2
while e < phi:
    if gcd(e, phi) == 1:
        break
    e += 1

def mod_inverse(e, phi):
    for d in range(1, phi):
        if (d * e) % phi == 1:
            return d
    return None

d = mod_inverse(e, phi)

public_key = (e, n)
private_key = (d, n)

def encrypt(plaintext, public_key):
    e, n = public_key
    cipher_numbers = [pow(ord(char), e, n) for char in plaintext]
    cipher_bytes = b''.join(num.to_bytes((num.bit_length() + 7) // 8, 'big') for num in cipher_numbers)
    cipher_text = base64.b64encode(cipher_bytes).decode()
    return cipher_text

def decrypt(cipher_text, private_key):
    d, n = private_key
    cipher_bytes = base64.b64decode(cipher_text)
    numbers = []
    i = 0
    while i < len(cipher_bytes):
        num = cipher_bytes[i]
        if i + 1 < len(cipher_bytes) and cipher_bytes[i + 1] != 0:
            num = (num << 8) + cipher_bytes[i + 1]
            i += 1
        numbers.append(num)
        i += 1
    plaintext = ''.join([chr(pow(num, d, n)) for num in numbers])
    return plaintext

message = input("Enter plaintext message: ")
encrypted_msg = encrypt(message, public_key)
print("Encrypted message:", encrypted_msg)
decrypted_msg = decrypt(encrypted_msg, private_key)
print("Decrypted message:", decrypted_msg)
print(f"public key:{public_key}")
print(f"private key:{private_key}")
