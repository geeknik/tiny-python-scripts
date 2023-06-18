import requests
import json

def lookup_data(ip_address):
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    return response.json()

def save_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_data(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def ip_lookup(ip_address, filename):
    data = lookup_data(ip_address)
    save_data(data, filename)

if __name__ == "__main__":
    ip_address = input("Enter the IP address: ")
    filename = "ip_data.json"
    ip_lookup(ip_address, filename)
    data = load_data(filename)
    print(data)
