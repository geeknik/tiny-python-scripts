
import os
import magic

def file_format_analysis(file_path):
    if not os.path.isfile(file_path):
        print(f"{file_path} does not exist.")
        return

    file_info = magic.from_file(file_path)
    print(f"File Info: {file_info}")

if __name__ == "__main__":
    file_path = input("Enter the path of the file: ")
    file_format_analysis(file_path)
