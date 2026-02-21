import os
from cryptography.fernet import Fernet

def generate_key():
    """Generates a new encryption key and saves it to a file."""
    key = Fernet.generate_key()
    with open("filekey.key", "wb") as key_file:
        key_file.write(key)
    print("Encryption key generated and saved to filekey.key")

def load_key():
    """Loads the encryption key from the current directory."""
    return open("filekey.key", "rb").read()

def encrypt_file(filepath):
    """Encrypts a file using the loaded key."""
    key = load_key()
    f = Fernet(key)
    with open(filepath, "rb") as file:
        file_data = file.read()
    encrypted_data = f.encrypt(file_data)
    with open(filepath + ".encrypted", "wb") as file:
        file.write(encrypted_data)
    print(f"File {filepath} encrypted to {filepath}.encrypted")

def decrypt_file(filepath):
    """Decrypts an encrypted file using the loaded key."""
    key = load_key()
    f = Fernet(key)
    with open(filepath, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
    with open(filepath.replace(".encrypted", ".decrypted"), "wb") as file:
        file.write(decrypted_data)
    print(f"File {filepath} decrypted to {filepath.replace('.encrypted', '.decrypted')}")

if __name__ == "__main__":
    print("\n--- Local File Encryption Script ---")
    print("Usage: python encrypt_file.py [generate_key|encrypt <filepath>|decrypt <filepath>]")
    
    # Example usage (uncomment to test):
    # generate_key()
    # encrypt_file("my_secret_document.txt")
    # decrypt_file("my_secret_document.txt.encrypted")

    # Basic command-line argument parsing
    import sys
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "generate_key":
            generate_key()
        elif command == "encrypt" and len(sys.argv) > 2:
            encrypt_file(sys.argv[2])
        elif command == "decrypt" and len(sys.argv) > 2:
            decrypt_file(sys.argv[2])
        else:
            print("Invalid command or missing filepath.")
    else:
        print("No command provided. Use 'generate_key', 'encrypt <filepath>', or 'decrypt <filepath>'.")

    print("\nNOTE: Requires 'cryptography' library. Install with: pip install cryptography")
