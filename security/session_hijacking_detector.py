import requests
from bs4 import BeautifulSoup

def check_session_hijacking(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        if 'Set-Cookie' in response.headers:
            cookie = response.headers['Set-Cookie']
            if 'Secure' in cookie and 'HttpOnly' in cookie:
                return "No signs of session hijacking vulnerability"
            else:
                return "Potential session hijacking vulnerability detected"
        else:
            return "No Set-Cookie header found"
    except requests.exceptions.RequestException as e:
        return str(e)

def main():
    url = input("Enter the URL to check for session hijacking vulnerability: ")
    result = check_session_hijacking(url)
    print(result)

if __name__ == "__main__":
    main()
