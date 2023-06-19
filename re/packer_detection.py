
import pefile
import os

def packer_detection(file_path):
    try:
        pe = pefile.PE(file_path)
        if hasattr(pe, 'DIRECTORY_ENTRY_IMPORT'):
            for entry in pe.DIRECTORY_ENTRY_IMPORT:
                if entry.dll.decode('utf-8').lower() in ['packer.dll', 'upx.dll']:
                    return True
        return False
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return False

if __name__ == "__main__":
    file_path = input("Enter the path of the file to check for packer: ")
    if os.path.isfile(file_path):
        is_packed = packer_detection(file_path)
        if is_packed:
            print("The file is packed.")
        else:
            print("The file is not packed.")
    else:
        print("The file does not exist.")
