import requests
from bs4 import BeautifulSoup

def extract_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.prettify()

def save_data(data, filename):
    with open(filename, 'w') as file:
        file.write(data)

def website_scraper(url, filename):
    data = extract_data(url)
    save_data(data, filename)

if __name__ == "__main__":
    url = input("Enter the URL to scrape: ")
    filename = input("Enter the filename to save the data: ")
    website_scraper(url, filename)
