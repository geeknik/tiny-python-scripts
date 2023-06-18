import requests
from geolite2 import geolite2

def extract_info(ip_address):
    reader = geolite2.reader()
    location_data = reader.get(ip_address)
    geolite2.close()
    return location_data

def save_results(ip_address, location_data):
    with open(f'{ip_address}_geolocation_data.txt', 'w') as f:
        f.write(str(location_data))

def main():
    ip_address = input("Enter the IP address: ")
    location_data = extract_info(ip_address)
    save_results(ip_address, location_data)

if __name__ == "__main__":
    main()
