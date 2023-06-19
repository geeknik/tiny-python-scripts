
import os
import subprocess

def check_for_updates():
    try:
        result = subprocess.check_output(['apt-get', 'update'])
        print(result)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def upgrade_packages():
    try:
        result = subprocess.check_output(['apt-get', 'upgrade', '-y'])
        print(result)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def main():
    check_for_updates()
    upgrade_packages()

if __name__ == "__main__":
    main()

