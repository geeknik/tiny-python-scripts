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
