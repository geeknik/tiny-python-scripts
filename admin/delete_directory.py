import os
import sys

def delete_directory(directory_path):
    try:
        if os.path.exists(directory_path):
            os.rmdir(directory_path)
            print(f"Directory {directory_path} deleted successfully.")
        else:
            print(f"Directory {directory_path} does not exist.")
    except Exception as e:
        print(f"An error occurred while deleting directory {directory_path}: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python delete_directory.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    delete_directory(directory_path)