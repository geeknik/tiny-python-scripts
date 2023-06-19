
import hashlib

def generate_hash(file_path, hash_type):
    try:
        with open(file_path, 'rb') as file:
            bytes = file.read()
            if hash_type == 'md5':
                readable_hash = hashlib.md5(bytes).hexdigest()
            elif hash_type == 'sha1':
                readable_hash = hashlib.sha1(bytes).hexdigest()
            elif hash_type == 'sha256':
                readable_hash = hashlib.sha256(bytes).hexdigest()
            else:
                print("Invalid hash type. Please choose from 'md5', 'sha1', or 'sha256'.")
                return None
            return readable_hash
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return None

def main():
    file_path = input("Enter the path of the file: ")
    hash_type = input("Enter the type of hash (md5, sha1, sha256): ")
    hash = generate_hash(file_path, hash_type)
    if hash is not None:
        print(f"The {hash_type} hash of the file is: {hash}")

if __name__ == "__main__":
    main()
