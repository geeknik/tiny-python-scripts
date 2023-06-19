
import os
import subprocess

def dynamic_analysis(file_path):
    # Check if the file exists
    if not os.path.isfile(file_path):
        print(f"The file {file_path} does not exist.")
        return

    # Use the 'strings' command to extract strings from the binary
    strings_output = subprocess.check_output(f"strings {file_path}", shell=True)
    print("Strings found in the binary:")
    print(strings_output.decode())

    # Use the 'ltrace' command to trace library calls
    ltrace_output = subprocess.check_output(f"ltrace {file_path}", shell=True)
    print("Library calls:")
    print(ltrace_output.decode())

    # Use the 'strace' command to trace system calls
    strace_output = subprocess.check_output(f"strace {file_path}", shell=True)
    print("System calls:")
    print(strace_output.decode())

if __name__ == "__main__":
    file_path = input("Enter the path of the binary file for dynamic analysis: ")
    dynamic_analysis(file_path)
