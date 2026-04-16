import hashlib
import secrets

# Generate a pepper (in real apps, this should be fixed & secret)
PEPPER = secrets.token_hex(16)

def hash_password(password):
    # Generate random salt
    salt = secrets.token_hex(16)
    
    # Combine password + salt + pepper
    combined = password + salt + PEPPER
    
    # Hash the combined string
    hashed = hashlib.sha256(combined.encode()).hexdigest()
    
    return salt, hashed

def verify_password(input_password, salt, stored_hash):
    combined = input_password + salt + PEPPER
    hashed = hashlib.sha256(combined.encode()).hexdigest()
    
    return hashed == stored_hash


# Step 1: User creates password
password = input("Create a password: ")

salt, hashed_password = hash_password(password)

print("\n--- Stored Credentials ---")
print("Salt:", salt)
print("Pepper:", PEPPER)
print("Hashed Password:", hashed_password)

# Step 2: User tries to login
print("\n--- Login ---")
login_password = input("Enter your password: ")

if verify_password(login_password, salt, hashed_password):
    print("✅ Login successful!")
else:
    print("❌ Incorrect password!")