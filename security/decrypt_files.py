from cryptography.fernet import Fernet

def load_key():
    """
    Load the previously generated key
    """
    return open("secret.key", "rb").read()

def decrypt_message(encrypted_message):
    """
    Decrypts an encrypted message
    """
    key = load_key()
    f = Fernet(key)
    decrypted_message = f.decrypt(encrypted_message)

    return decrypted_message

def main():
    encrypted_message = input("Enter the encrypted message: ")
    print("Decrypted message: ", decrypt_message(encrypted_message))

if __name__ == "__main__":
    main()