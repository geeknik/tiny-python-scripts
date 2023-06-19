
import os
import subprocess

def detect_rootkit():
    # List of known rootkits
    known_rootkits = ['chkrootkit', 'rkhunter', 'lynis']

    # Check if any known rootkit is installed
    for rootkit in known_rootkits:
        try:
            result = subprocess.check_output(['which', rootkit])
            if result:
                print(f"{rootkit} is installed.")
        except subprocess.CalledProcessError:
            print(f"{rootkit} is not installed.")

    # Check for hidden files in system directories
    system_dirs = ['/bin', '/sbin', '/usr/bin', '/usr/sbin']
    for dir in system_dirs:
        try:
            hidden_files = subprocess.check_output(['find', dir, '-name', '.*'])
            if hidden_files:
                print(f"Hidden files found in {dir}:")
                print(hidden_files)
        except subprocess.CalledProcessError:
            print(f"No hidden files in {dir}.")

if __name__ == "__main__":
    detect_rootkit()
