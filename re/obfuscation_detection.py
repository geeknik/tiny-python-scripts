
import os
import re

def detect_obfuscation(file_path):
    obfuscation_patterns = [
        r'\b(eval|exec|compile)\b',  # Dynamic code execution
        r'\b(base64)\b',  # Base64 encoding
        r'\b(rot13)\b',  # ROT13 encoding
        r'\b(xor)\b',  # XOR cipher
        r'\b(chr|ord)\b',  # Character manipulation
        r'\b(__import__)\b',  # Dynamic imports
    ]

    with open(file_path, 'r') as file:
        content = file.read()

    for pattern in obfuscation_patterns:
        if re.search(pattern, content):
            print(f"Potential obfuscation detected in {file_path} with pattern: {pattern}")

if __name__ == "__main__":
    file_path = input("Enter the path of the file to analyze: ")
    detect_obfuscation(file_path)
