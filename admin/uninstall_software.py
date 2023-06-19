
import subprocess
import sys

def uninstall_software(software_name):
    try:
        subprocess.check_call(["sudo", "apt-get", "remove", software_name])
        print(f"{software_name} has been successfully uninstalled.")
    except subprocess.CalledProcessError:
        print(f"Failed to uninstall {software_name}.")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python uninstall_software.py [software_name]")
        sys.exit(1)
    uninstall_software(sys.argv[1])
