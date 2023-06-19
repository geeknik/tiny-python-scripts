
import os
import sys

def change_owner(filename, user, group=None):
    try:
        os.chown(filename, user, group if group else user)
    except FileNotFoundError:
        print(f"File {filename} not found.")
        sys.exit(1)
    except PermissionError:
        print("Permission denied.")
        sys.exit(1)
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: change_owner.py <filename> <user> <group>")
        sys.exit(1)

    filename = sys.argv[1]
    user = int(sys.argv[2])
    group = int(sys.argv[3])

    change_owner(filename, user, group)
