
import os
import shutil
import sys

def restore_files(backup_dir, restore_dir):
    try:
        # Check if backup directory exists
        if not os.path.exists(backup_dir):
            print(f"Backup directory {backup_dir} does not exist.")
            return

        # Check if restore directory exists
        if not os.path.exists(restore_dir):
            os.makedirs(restore_dir)

        # Copy files from backup directory to restore directory
        for filename in os.listdir(backup_dir):
            shutil.copy(os.path.join(backup_dir, filename), restore_dir)

        print(f"Files restored from {backup_dir} to {restore_dir}.")

    except Exception as e:
        print(f"An error occurred while restoring files: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python restore_files.py <backup_dir> <restore_dir>")
        sys.exit(1)

    backup_dir = sys.argv[1]
    restore_dir = sys.argv[2]

    restore_files(backup_dir, restore_dir)
