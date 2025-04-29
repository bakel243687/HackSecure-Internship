from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    print(f"Key generated and saved to {KEY_FILE}")
    return key

def load_key():
    if not os.path.exists(KEY_FILE):
        print("Key file not found. Generating a new one...")
        return generate_key()
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()

def encrypt_file(input_file, output_file, key):
    fernet = Fernet(key)
    with open(input_file, "rb") as f:
        data = f.read()
    encrypted = fernet.encrypt(data)
    with open(output_file, "wb") as f:
        f.write(encrypted)
    print(f"File encrypted and saved as {output_file}")

def decrypt_file(input_file, output_file, key):
    fernet = Fernet(key)
    with open(input_file, "rb") as f:
        encrypted_data = f.read()
    try:
        decrypted = fernet.decrypt(encrypted_data)
        with open(output_file, "wb") as f:
            f.write(decrypted)
        print(f"File decrypted and saved as {output_file}")
    except Exception as e:
        print("Failed to decrypt. Error:", str(e))

def main():
    print("=== File Encryption/Decryption Tool ===")
    choice = input("Choose an option (E)ncrypt or (D)ecrypt: ").strip().lower()

    if choice not in ['e', 'd']:
        print("Invalid option. Use 'E' or 'D'.")
        return

    input_file = input("Enter the path to the input file: ").strip()
    output_file = input("Enter the path to save the output file: ").strip()

    if not os.path.exists(input_file):
        print("Input file not found.")
        return

    key = load_key()

    if choice == 'e':
        encrypt_file(input_file, output_file, key)
    else:
        decrypt_file(input_file, output_file, key)

if __name__ == "__main__":
    main()
