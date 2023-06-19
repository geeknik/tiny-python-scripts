
import os

def create_directory(directory_path):
    try:
        os.makedirs(directory_path)
        print(f"Directory {directory_path} created successfully")
    except FileExistsError:
        print(f"Directory {directory_path} already exists")
    except Exception as e:
        print(f"Error occurred while creating directory {directory_path}: {str(e)}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python create_directory.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    create_directory(directory_path)
