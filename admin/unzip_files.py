
import os
import zipfile

def unzip_files(zip_filepath, dest_dir):
    try:
        with zipfile.ZipFile(zip_filepath, 'r') as zip_ref:
            zip_ref.extractall(dest_dir)
        print(f"Files extracted successfully to {dest_dir}")
    except FileNotFoundError:
        print(f"Zip file {zip_filepath} not found.")
    except PermissionError:
        print(f"Permission denied to write to {dest_dir}.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python unzip_files.py <zip_filepath> <dest_dir>")
        sys.exit(1)

    zip_filepath = sys.argv[1]
    dest_dir = sys.argv[2]
    unzip_files(zip_filepath, dest_dir)
