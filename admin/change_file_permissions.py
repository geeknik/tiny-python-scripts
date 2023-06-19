
import os
import sys

def change_file_permissions(filepath, permissions):
    try:
        os.chmod(filepath, permissions)
    except FileNotFoundError:
        print(f"File {filepath} not found.")
        sys.exit(1)
    except PermissionError:
        print(f"Insufficient permissions to change the file {filepath}.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python change_file_permissions.py <filepath> <permissions>")
        sys.exit(1)

    filepath = sys.argv[1]
    permissions = int(sys.argv[2], 8)

    change_file_permissions(filepath, permissions)
