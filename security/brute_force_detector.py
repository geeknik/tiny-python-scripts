
import time
from collections import Counter

def detect_brute_force(log_file):
    with open(log_file, 'r') as file:
        logs = file.readlines()

    ip_list = [log.split()[0] for log in logs]
    count = Counter(ip_list)

    for ip, freq in count.items():
        if freq > 100:  # threshold for brute force detection
            print(f"Potential brute force attack detected from IP: {ip}")

def main():
    log_file = 'access.log'  # replace with your log file
    detect_brute_force(log_file)

if __name__ == "__main__":
    main()
```
This script reads a log file, counts the number of requests from each IP address, and if the number of requests from a single IP exceeds a certain threshold (100 in this case), it flags that IP as a potential source of a brute force attack.