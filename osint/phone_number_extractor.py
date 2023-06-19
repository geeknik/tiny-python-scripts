import re
import requests
from bs4 import BeautifulSoup

def extract_phone_numbers(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    phone_numbers = re.findall(r'\(?\b[2-9][0-9]{2}\)?[-. ]?[2-9][0-9]{2}[-. ]?[0-9]{4}\b', soup.text)
    return phone_numbers

if __name__ == "__main__":
    url = input("Enter the URL: ")
    phone_numbers = extract_phone_numbers(url)
    print("Phone Numbers found: ", phone_numbers)
