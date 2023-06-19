import shutil
import sys
import os

def copy_files(src, dest):
    try:
        shutil.copy2(src, dest)
        print(f"File {src} copied to {dest}")
    except FileNotFoundError:
        print(f"Source file {src} not found.")
    except PermissionError:
        print(f"Permission denied.")
    except Exception as e:
        print(f"Unable to copy file. Error: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python copy_files.py <source> <destination>")
        sys.exit(1)

    source = sys.argv[1]
    destination = sys.argv[2]

    if not os.path.isfile(source):
        print(f"Source file {source} does not exist.")
        sys.exit(1)

    copy_files(source, destination)