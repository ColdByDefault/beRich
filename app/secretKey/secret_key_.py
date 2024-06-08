import secrets

# Generate a random URL-safe text string for a secret key
secret_key = secrets.token_urlsafe(16)
print("Secret Key:", secret_key)
