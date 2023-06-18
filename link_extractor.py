import requests
from bs4 import BeautifulSoup
import re

def extract_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    links = [a['href'] for a in soup.find_all('a', href=True)]
    return links

def save_data(links, filename):
    with open(filename, 'w') as f:
        for link in links:
            f.write("%s\n" % link)

def main():
    url = input("Enter the URL: ")
    links = extract_links(url)
    save_data(links, 'extracted_links.txt')

if __name__ == "__main__":
    main()
