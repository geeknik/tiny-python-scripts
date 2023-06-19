
from cryptography.fernet import Fernet

def automated_decryption(ciphertext, key):
    cipher_suite = Fernet(key)
    plaintext = cipher_suite.decrypt(ciphertext)
    return plaintext

if __name__ == "__main__":
    key = Fernet.generate_key()  # this should be stored securely
    cipher_suite = Fernet(key)
    ciphertext = cipher_suite.encrypt(b"Hello World!")  # bytes
    print("Ciphertext:", ciphertext)

    plaintext = automated_decryption(ciphertext, key)
    print("Decrypted Text:", plaintext.decode())
