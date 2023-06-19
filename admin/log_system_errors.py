
import os
import sys
import logging
from datetime import datetime

def log_system_errors():
    log_file = "/var/log/syslog"
    error_log_file = "system_errors.log"

    if not os.path.exists(log_file):
        print(f"Log file {log_file} does not exist.")
        sys.exit(1)

    with open(log_file, "r") as file:
        lines = file.readlines()

    with open(error_log_file, "w") as file:
        for line in lines:
            if "error" in line.lower():
                file.write(line)

    print(f"System errors have been logged in {error_log_file}.")

if __name__ == "__main__":
    log_system_errors()
