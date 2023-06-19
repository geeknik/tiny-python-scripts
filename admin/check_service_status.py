
import subprocess

def check_service_status(service_name):
    try:
        output = subprocess.check_output(
            "systemctl is-active --quiet " + service_name, shell=True
        )
        if output == b'active\n':
            print(f"The {service_name} is running.")
        else:
            print(f"The {service_name} is not running.")
    except subprocess.CalledProcessError:
        print(f"Failed to get the status of {service_name}.")

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python check_service_status.py <service_name>")
        sys.exit(1)
    check_service_status(sys.argv[1])
