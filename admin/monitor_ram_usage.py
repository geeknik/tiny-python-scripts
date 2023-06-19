
import psutil

def monitor_ram_usage():
    memory_info = psutil.virtual_memory()
    total_memory = memory_info.total / (1024.0 ** 3)
    available_memory = memory_info.available / (1024.0 ** 3)
    used_memory = memory_info.used / (1024.0 ** 3)
    memory_percentage = memory_info.percent

    print(f"Total Memory: {total_memory} GB")
    print(f"Available Memory: {available_memory} GB")
    print(f"Used Memory: {used_memory} GB")
    print(f"Memory Usage: {memory_percentage}%")

if __name__ == "__main__":
    monitor_ram_usage()
