import requests
from bs4 import BeautifulSoup

def csrf_detector(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        forms = soup.find_all('form')
        for form in forms:
            if not form.get('csrf-token'):
                return "Potential CSRF vulnerability detected in form: {}".format(form)
        return "No CSRF vulnerabilities detected."
    except Exception as e:
        return "Error occurred: {}".format(e)

def main():
    url = input("Enter the URL to scan for CSRF vulnerabilities: ")
    result = csrf_detector(url)
    print(result)

if __name__ == "__main__":
    main()
