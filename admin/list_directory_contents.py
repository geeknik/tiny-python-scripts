import os

def list_directory_contents(directory_path):
    try:
        # Check if the directory exists
        if not os.path.isdir(directory_path):
            print(f"The directory {directory_path} does not exist.")
            return

        # List the contents of the directory
        directory_contents = os.listdir(directory_path)

        # Print the contents of the directory
        for content in directory_contents:
            print(content)

    except Exception as e:
        print(f"An error occurred while listing the contents of the directory: {e}")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python list_directory_contents.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    list_directory_contents(directory_path)