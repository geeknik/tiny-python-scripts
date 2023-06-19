
import subprocess

def detect_vm():
    try:
        result = subprocess.check_output('dmidecode -t system', shell=True)
        if 'VMware' in result or 'VirtualBox' in result:
            return True
        else:
            return False
    except Exception as e:
        print("An error occurred: ", e)
        return False

if __name__ == "__main__":
    if detect_vm():
        print("Virtual Machine Detected!")
    else:
        print("No Virtual Machine Detected.")
