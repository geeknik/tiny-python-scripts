
import os
import hashlib
from binascii import hexlify

def static_analysis(file_path):
    # Check if file exists
    if not os.path.exists(file_path):
        print("File does not exist")
        return

    # Get file size
    file_size = os.path.getsize(file_path)
    print(f"File Size is : {file_size} bytes")

    # Get file checksum
    with open(file_path, "rb") as f:
        bytes = f.read() # read entire file as bytes
        readable_hash = hashlib.md5(bytes).hexdigest();
        print(f"File Checksum is : {readable_hash}")

    # Get file metadata
    file_stats = os.stat(file_path)
    print(f"File Last Modified On : {file_stats.st_mtime}")

    # Get file content in hex
    with open(file_path, 'rb') as f:
        content = f.read()
    hex_content = hexlify(content)
    print(f"File Content in Hex : {hex_content}")

# Test the function
static_analysis("test_file.txt")
