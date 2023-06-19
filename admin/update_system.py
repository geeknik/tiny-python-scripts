
import os
import subprocess

def update_system():
    try:
        print("Updating system...")
        subprocess.check_call(['sudo', 'apt-get', 'update'])
        subprocess.check_call(['sudo', 'apt-get', 'upgrade', '-y'])
        print("System update completed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"System update failed: {e}")
        return 1

    return 0

if __name__ == "__main__":
    update_system()
