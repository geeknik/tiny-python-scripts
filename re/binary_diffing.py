
import os
import difflib

def binary_diff(file1, file2):
    with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
        file1_data = f1.read()
        file2_data = f2.read()

    file1_lines = str(file1_data).splitlines()
    file2_lines = str(file2_data).splitlines()

    diff = difflib.unified_diff(file1_lines, file2_lines)

    return '\n'.join(list(diff))

if __name__ == "__main__":
    file1 = input("Enter the path of the first binary file: ")
    file2 = input("Enter the path of the second binary file: ")

    if not os.path.isfile(file1):
        print(f"{file1} does not exist.")
        exit(1)

    if not os.path.isfile(file2):
        print(f"{file2} does not exist.")
        exit(1)

    print(binary_diff(file1, file2))
