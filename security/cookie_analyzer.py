
import requests
from bs4 import BeautifulSoup

def analyze_cookies(url):
    response = requests.get(url)
    cookies = response.cookies
    for cookie in cookies:
        print(f"Name: {cookie.name}")
        print(f"Value: {cookie.value}")
        print(f"Domain: {cookie.domain}")
        print(f"Path: {cookie.path}")
        print(f"Secure: {cookie.secure}")
        print(f"Expires: {cookie.expires}")
        print(f"Discard: {cookie.discard}")
        print(f"Comment: {cookie.comment}")
        print(f"Comment URL: {cookie.comment_url}")
        print(f"Rest: {cookie._rest}")
        print(f"RFC2109: {cookie.rfc2109}")
        print("\n")

def main():
    url = input("Enter the URL to analyze cookies: ")
    analyze_cookies(url)

if __name__ == "__main__":
    main()
