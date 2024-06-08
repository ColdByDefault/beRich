import secrets

# Generate a random URL-safe text string for a secret key
secret_key = secrets.token_urlsafe(16)
print("Secret Key:", secret_key)






# Generate a 32-byte (256-bit) random secret key
csrf_secret_key = secrets.token_hex(32)
print(csrf_secret_key)

