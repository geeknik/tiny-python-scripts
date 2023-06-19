
import os
import binascii

def side_channel_analysis(file_path):
    try:
        with open(file_path, 'rb') as file:
            data = file.read()
            hex_data = binascii.hexlify(data)
            print(f"Hex Data: {hex_data}")
            
            # Frequency analysis
            frequency = dict()
            for byte in hex_data:
                if byte not in frequency:
                    frequency[byte] = 0
                frequency[byte] += 1
            
            print("Frequency Analysis:")
            for byte, freq in frequency.items():
                print(f"{byte}: {freq}")
                
    except FileNotFoundError:
        print(f"{file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Test the function
side_channel_analysis("test_file.bin")
