import hashlib

def hash_file(filename):
    h = hashlib.sha3_256()
    h1 = hashlib.sha3_384()
    h2 = hashlib.sha3_512()

    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            h.update(chunk)
            h1.update(chunk)
            h2.update(chunk)

    return h.hexdigest(), h1.hexdigest(), h2.hexdigest()

def main():
    sha3_256, sha3_384, sha3_512 = hash_file("example.txt")
    print("SHA3-256:", sha3_256)
    print("SHA3-384:", sha3_384)
    print("SHA3-512:", sha3_512)

if __name__ == "__main__":
    main()
