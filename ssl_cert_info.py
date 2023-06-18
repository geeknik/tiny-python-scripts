import ssl
import socket
import json

def extract_info(hostname):
    context = ssl.create_default_context()
    conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=hostname)
    conn.settimeout(3.0)
    conn.connect((hostname, 443))
    ssl_info = conn.getpeercert()
    return ssl_info

def save_results(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

def main():
    hostname = 'www.example.com'
    ssl_info = extract_info(hostname)
    save_results(ssl_info, 'ssl_info.json')

if __name__ == "__main__":
    main()
