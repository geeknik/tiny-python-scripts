
import socket

def scan_ports(host):
    open_ports = []
    for port in range(1, 65535):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((host, port))
        if result == 0:
            open_ports.append(port)
        sock.close()
    return open_ports

def main():
    host = input("Enter the host to scan: ")
    open_ports = scan_ports(host)
    print(f"Open ports on {host}: {open_ports}")

if __name__ == "__main__":
    main()
