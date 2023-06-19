
import os
import hashlib

def calculate_hash(file_path):
    BUF_SIZE = 65536
    sha256 = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

def scan_directory(directory):
    ransomware_signatures = load_ransomware_signatures()
    for foldername, subfolders, filenames in os.walk(directory):
        for filename in filenames:
            file_path = os.path.join(foldername, filename)
            file_hash = calculate_hash(file_path)
            if file_hash in ransomware_signatures:
                print(f'Ransomware detected: {file_path}')

def load_ransomware_signatures():
    with open('ransomware_signatures.txt', 'r') as f:
        signatures = f.read().splitlines()
    return signatures

def main():
    directory_to_scan = '/path/to/directory'
    scan_directory(directory_to_scan)

if __name__ == "__main__":
    main()
```
This script scans a directory for files that match known ransomware signatures. The signatures are loaded from a text file named `ransomware_signatures.txt`, where each line is a SHA-256 hash of a known ransomware file. The script walks through every file in the specified directory and its subdirectories, calculates the SHA-256 hash of each file, and checks if the hash is in the list of known ransomware signatures. If a match is found, the script prints a message indicating that ransomware has been detected.