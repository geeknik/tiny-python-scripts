
import psutil
import time

def monitor_network_traffic():
    old_value = 0

    while True:
        new_value = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv

        if old_value:
            send_stat(new_value - old_value)

        old_value = new_value

        time.sleep(1)

def send_stat(value):
    print(f"Network traffic: {value} bytes/s")

if __name__ == "__main__":
    monitor_network_traffic()
