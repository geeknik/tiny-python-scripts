
import os
import re

def detect_code_injection(file_path):
    try:
        with open(file_path, 'r') as file:
            data = file.read()
            # Regular expression pattern for common code injection payloads
            patterns = [
                re.compile(r'<\?php', re.I),
                re.compile(r'eval\(', re.I),
                re.compile(r'base64_decode\(', re.I),
                re.compile(r'python exec\(', re.I),
                re.compile(r'javascript:eval\(', re.I),
                re.compile(r'fromCharCode\(', re.I),
                re.compile(r'document\.write\(', re.I),
                re.compile(r'window\.location\=', re.I),
                re.compile(r'innerHTML\=', re.I),
            ]
            for pattern in patterns:
                if pattern.search(data):
                    print(f'Possible code injection detected in {file_path}')
                    return True
            print(f'No code injection detected in {file_path}')
            return False
    except FileNotFoundError:
        print(f'File {file_path} not found.')
        return False

if __name__ == "__main__":
    detect_code_injection('test_file.php')
