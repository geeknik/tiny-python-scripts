
import os
import sys
import shutil

def check_disk_space():
    total, used, free = shutil.disk_usage("/")
    
    print("Total: %d GiB" % (total // (2**30)))
    print("Used: %d GiB" % (used // (2**30)))
    print("Free: %d GiB" % (free // (2**30)))

if __name__ == "__main__":
    check_disk_space()
