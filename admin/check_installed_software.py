
import subprocess

def check_installed_software(software_name):
    try:
        output = subprocess.check_output("dpkg -s " + software_name, shell=True)
        if "install ok installed" in output:
            print(software_name + " is installed.")
        else:
            print(software_name + " is not installed.")
    except subprocess.CalledProcessError:
        print(software_name + " is not installed.")

if __name__ == "__main__":
    software_name = input("Enter the name of the software to check: ")
    check_installed_software(software_name)
