import requests
import json

def extract_subdomains(domain, api_key):
    url = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"
    headers = {
        "APIKEY": api_key
    }
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    subdomains = [f"{sub}.{domain}" for sub in data.get('subdomains', [])]
    return subdomains

def save_results(subdomains, domain):
    with open(f"{domain}_subdomains.txt", 'w') as f:
        for subdomain in subdomains:
            f.write(f"{subdomain}\n")

def main(domain, api_key):
    subdomains = extract_subdomains(domain, api_key)
    save_results(subdomains, domain)

if __name__ == "__main__":
    domain = input("Enter the domain: ")
    api_key = "YOUR_API_KEY"
    main(domain, api_key)
