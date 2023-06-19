
import pefile
import os

def detect_anti_disassembly(file_path):
    try:
        pe = pefile.PE(file_path)
    except OSError as e:
        print(e)
        return
    except pefile.PEFormatError as e:
        print("[-] PEFormatError: %s" % e.value)
        return

    # Check for UPX packed files
    if pe.OPTIONAL_HEADER.DATA_DIRECTORY[pefile.DIRECTORY_ENTRY['IMAGE_DIRECTORY_ENTRY_IMPORT']].VirtualAddress == 0:
        print("[+] The file is packed with UPX.")
    else:
        print("[-] The file is not packed with UPX.")

    # Check for Section Overlapping, which can cause disassemblers to fail
    for section in pe.sections:
        if section.PointerToRawData < pe.OPTIONAL_HEADER.SizeOfHeaders:
            print("[+] Section Overlapping detected. This can cause disassemblers to fail.")

    # Check for invalid entry point
    if pe.OPTIONAL_HEADER.AddressOfEntryPoint == 0:
        print("[+] Invalid Entry Point detected. This can cause disassemblers to fail.")

if __name__ == "__main__":
    file_path = input("Enter the path of the file to analyze: ")
    if os.path.exists(file_path):
        detect_anti_disassembly(file_path)
    else:
        print("The file does not exist.")
