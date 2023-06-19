
import os
import sys

def memory_dump(pid):
    try:
        mem_file = open("/proc/{}/mem".format(pid), 'rb')
    except FileNotFoundError:
        print("Process {} does not exist.".format(pid))
        sys.exit(1)

    try:
        maps_file = open("/proc/{}/maps".format(pid), 'r')
    except FileNotFoundError:
        print("Maps for process {} do not exist.".format(pid))
        sys.exit(1)

    for line in maps_file:
        sline = line.split(' ')
        s = sline[0].split('-')

        start = int(s[0], 16)
        end = int(s[1], 16)

        mem_file.seek(start)
        chunk = mem_file.read(end - start)

        out_file = open("dump_{}_{}_{}.dmp".format(pid, s[0], s[1]), 'wb')
        out_file.write(chunk)
        out_file.close()

    mem_file.close()
    maps_file.close()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python memory_dump.py <pid>")
        sys.exit(1)

    memory_dump(sys.argv[1])
