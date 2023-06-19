
import os
import zipfile

def zip_files(file_paths, zip_name):
    with zipfile.ZipFile(zip_name, 'w') as zipf:
        for file in file_paths:
            if os.path.isfile(file):
                zipf.write(file)
            else:
                print(f"File not found: {file}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python zip_files.py <zip_name> <file1> <file2> ...")
        sys.exit(1)

    zip_name = sys.argv[1]
    file_paths = sys.argv[2:]
    zip_files(file_paths, zip_name)
