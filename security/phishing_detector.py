
import requests
import validators
from bs4 import BeautifulSoup

def main():
    url = input("Enter the URL to check for phishing: ")
    if not validators.url(url):
        print("Invalid URL. Please enter a valid URL.")
        return
    response = get_response(url)
    if response is None:
        print("Failed to get a response from the URL.")
        return
    soup = BeautifulSoup(response.text, 'html.parser')
    if is_phishing(soup):
        print("The URL is potentially a phishing site.")
    else:
        print("The URL is not a phishing site.")

def get_response(url):
    try:
        return requests.get(url)
    except requests.exceptions.RequestException as e:
        print(e)
        return None

def is_phishing(soup):
    # Check for common phishing techniques in the HTML
    if len(soup.find_all('iframe')) > 0:
        return True
    if len(soup.find_all('input', type='password')) > 0:
        return True
    return False

if __name__ == "__main__":
    main()
