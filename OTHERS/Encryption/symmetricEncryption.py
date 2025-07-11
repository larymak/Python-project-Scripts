# simple_encryption.py

"""
A simple example of symmetric encryption using Python's 'cryptography' package.

This script:
1. Generates a secure encryption key
2. Encrypts a message using the key
3. Decrypts it back to the original message

Author: Afolabi Adewale
"""

from cryptography.fernet import Fernet

# 1. Generate a key for encryption and decryption
def generate_key():
    """
    Generates a symmetric key for Fernet (uses AES encryption internally).
    """
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)
    print("[+] Key generated and saved to 'secret.key'")
    return key

# 2. Load the existing key from file
def load_key():
    """
    Loads the previously generated key from the file.
    """
    return open("secret.key", "rb").read()

# 3. Encrypt a message
def encrypt_message(message: str, key: bytes) -> bytes:
    """
    Encrypts a message using the provided symmetric key.
    """
    f = Fernet(key)
    encrypted = f.encrypt(message.encode())
    return encrypted

# 4. Decrypt a message
def decrypt_message(encrypted_message: bytes, key: bytes) -> str:
    """
    Decrypts an encrypted message using the same symmetric key.
    """
    f = Fernet(key)
    decrypted = f.decrypt(encrypted_message)
    return decrypted.decode()

# 5. Main runner
if __name__ == "__main__":
    # Create or load the key
    try:
        key = load_key()
        print("[*] Key loaded from 'secret.key'")
    except FileNotFoundError:
        key = generate_key()

    # Example message
    message = "This is a secret message."
    print(f"\nOriginal Message: {message}")

    # Encrypt it
    encrypted = encrypt_message(message, key)
    print(f"Encrypted Message: {encrypted}")

    # Decrypt it
    decrypted = decrypt_message(encrypted, key)
    print(f"Decrypted Message: {decrypted}")
