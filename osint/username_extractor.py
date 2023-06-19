import requests
from bs4 import BeautifulSoup
import re

def extract_usernames(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    usernames = []

    for link in soup.find_all('a'):
        username = re.search(r'(?<=\/)([^\/]+$)', link.get('href'))
        if username:
            usernames.append(username.group())

    return usernames

if __name__ == "__main__":
    url = input("Enter the URL: ")
    usernames = extract_usernames(url)
    print("Extracted Usernames: ", usernames)
