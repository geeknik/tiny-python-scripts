import requests
import json

def extract_info(ssid):
    response = requests.get(f'https://api.mylnikov.org/geolocation/wifi?v=1.1&data=open&bssid={ssid}')
    data = json.loads(response.text)
    return data

def save_results(data, ssid):
    with open(f'{ssid}_location.json', 'w') as file:
        json.dump(data, file)

def main():
    ssid = input("Enter SSID: ")
    data = extract_info(ssid)
    save_results(data, ssid)

if __name__ == "__main__":
    main()
