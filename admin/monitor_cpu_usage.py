
import psutil
import time

def monitor_cpu_usage():
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        print(f'CPU Usage: {cpu_usage}%')
        time.sleep(5)

if __name__ == "__main__":
    monitor_cpu_usage()
