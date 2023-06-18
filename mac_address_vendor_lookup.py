import requests
import json

def extract_info(mac_address):
    url = f"https://api.macaddress.io/v1?apiKey=YOUR_API_KEY&output=json&search={mac_address}"
    response = requests.get(url)
    data = json.loads(response.text)
    return data['vendorDetails']

def save_results(mac_address, vendor_info):
    with open(f'{mac_address}_vendor_info.json', 'w') as file:
        json.dump(vendor_info, file)

def main():
    mac_address = input("Enter MAC Address: ")
    vendor_info = extract_info(mac_address)
    save_results(mac_address, vendor_info)

if __name__ == "__main__":
    main()
