
from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_file(filename):
    key = load_key()
    f = Fernet(key)

    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(filename, "wb") as file:
        file.write(encrypted_data)

if __name__ == "__main__":
    filename = input("Enter the name of the file to encrypt: ")
    if not os.path.isfile(filename):
        print(f"The file {filename} does not exist.")
    else:
        generate_key()
        encrypt_file(filename)
        print(f"The file {filename} has been encrypted.")
