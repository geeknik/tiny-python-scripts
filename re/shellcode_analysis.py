
import binascii

def shellcode_analysis(shellcode):
    try:
        # Convert shellcode to ascii
        ascii_shellcode = binascii.unhexlify(shellcode.replace("\\x", "")).decode('utf-8')
        print("ASCII Shellcode: ", ascii_shellcode)
        
        # Convert shellcode to binary
        binary_shellcode = bin(int(binascii.hexlify(ascii_shellcode.encode('utf-8')), 16))
        print("Binary Shellcode: ", binary_shellcode)
        
        # Frequency analysis
        frequency_analysis(ascii_shellcode)
        
    except Exception as e:
        print("An error occurred during shellcode analysis: ", str(e))

def frequency_analysis(data):
    frequency = {}
    for char in data:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    print("Frequency Analysis: ", frequency)
