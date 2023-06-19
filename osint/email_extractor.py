import re
import requests
from bs4 import BeautifulSoup

def extract_emails(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    mail_ids = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', soup.text)
    return mail_ids

if __name__ == "__main__":
    url = input("Enter the URL to extract emails from: ")
    emails = extract_emails(url)
    print(f"Found the following email addresses on {url}:")
    for email in emails:
        print(email)
