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
