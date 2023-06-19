import os
import subprocess

def update_antivirus():
    # Assuming the antivirus software is ClamAV
    try:
        print("Updating ClamAV antivirus...")
        subprocess.check_call(['freshclam'], stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        print("Update successful.")
    except subprocess.CalledProcessError:
        print("Update failed. Please check your internet connection and try again.")

def main():
    update_antivirus()

if __name__ == "__main__":
    main()
