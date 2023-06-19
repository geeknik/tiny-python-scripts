
import os
import sys

def delete_files(file_paths):
    for file_path in file_paths:
        try:
            os.remove(file_path)
            print(f"File {file_path} deleted successfully")
        except FileNotFoundError:
            print(f"File {file_path} does not exist")
        except PermissionError:
            print(f"Permission denied for deleting {file_path}")
        except Exception as e:
            print(f"Error occurred while deleting {file_path}: {str(e)}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide at least one file path to delete")
        sys.exit(1)

    file_paths = sys.argv[1:]
    delete_files(file_paths)
