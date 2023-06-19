
import os
import subprocess

def hardware_analysis():
    # Get the hardware details using lshw command
    hardware_details = subprocess.check_output(['lshw'], text=True)
    
    # Save the hardware details to a file
    with open('hardware_details.txt', 'w') as f:
        f.write(hardware_details)

    # Print the hardware details
    print(hardware_details)

if __name__ == "__main__":
    hardware_analysis()
