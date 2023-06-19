
import binascii
import re

def detect_encryption(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
        hex_data = binascii.hexlify(data)
        ascii_data = data.decode('ascii', errors='replace')

    # Check for Base64 encoding
    base64_pattern = r'^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$'
    if re.match(base64_pattern, ascii_data):
        return "Base64"

    # Check for Hex encoding
    hex_pattern = r'^[0-9a-fA-F]+$'
    if re.match(hex_pattern, ascii_data):
        return "Hex"

    # Check for ASCII encoding
    ascii_pattern = r'^[\x00-\x7F]+$'
    if re.match(ascii_pattern, ascii_data):
        return "ASCII"

    return "Unknown"

if __name__ == "__main__":
    file_path = input("Enter the file path: ")
    encryption_type = detect_encryption(file_path)
    print(f"The file is encoded in {encryption_type}")
