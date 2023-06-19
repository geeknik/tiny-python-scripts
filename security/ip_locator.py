import requests
import json

def get_ip_location(ip_address):
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    return response.json()

def main():
    ip_address = input("Enter the IP address: ")
    location_info = get_ip_location(ip_address)
    print(json.dumps(location_info, indent=4))

if __name__ == "__main__":
    main()