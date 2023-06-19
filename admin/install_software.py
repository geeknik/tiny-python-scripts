
import subprocess
import sys

def install_software(software_name):
    try:
        subprocess.check_call(['sudo', 'apt-get', 'install', '-y', software_name])
        print(f"{software_name} installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to install {software_name}. Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python install_software.py <software_name>")
        sys.exit(1)
    install_software(sys.argv[1])
