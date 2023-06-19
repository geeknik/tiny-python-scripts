
import os
import shutil
import datetime

def backup_files(source_directory, backup_directory):
    try:
        # Check if source directory exists
        if not os.path.exists(source_directory):
            raise FileNotFoundError(f"Source directory {source_directory} does not exist")

        # Create backup directory if it does not exist
        if not os.path.exists(backup_directory):
            os.makedirs(backup_directory)

        # Get current date and time to create a unique backup directory
        current_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        backup_subdirectory = os.path.join(backup_directory, current_time)

        # Create backup subdirectory
        os.makedirs(backup_subdirectory)

        # Copy files from source directory to backup directory
        for filename in os.listdir(source_directory):
            source_file = os.path.join(source_directory, filename)
            destination_file = os.path.join(backup_subdirectory, filename)
            shutil.copy2(source_file, destination_file)

        print(f"Backup of files from {source_directory} completed successfully at {backup_subdirectory}")

    except Exception as e:
        print(f"An error occurred while backing up files: {str(e)}")

if __name__ == "__main__":
    source_directory = "/path/to/source/directory"
    backup_directory = "/path/to/backup/directory"
    backup_files(source_directory, backup_directory)
