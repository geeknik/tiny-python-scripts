
import os
import shutil
import sys

def move_files(source_path, destination_path):
    try:
        shutil.move(source_path, destination_path)
        print(f"File moved from {source_path} to {destination_path}")
    except Exception as e:
        print(f"Error occurred while moving file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python move_files.py <source_path> <destination_path>")
        sys.exit(1)

    source_path = sys.argv[1]
    destination_path = sys.argv[2]
    move_files(source_path, destination_path)
