import socket
import json

def dns_lookup(domain):
    try:
        ip = socket.gethostbyname(domain)
        return ip
    except socket.gaierror as e:
        return str(e)

def main():
    domain = input("Enter the domain: ")
    ip = dns_lookup(domain)
    print(f"IP address of {domain} is {ip}")

if __name__ == "__main__":
    main()
