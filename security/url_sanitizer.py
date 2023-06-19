import validators
import urllib.parse

def sanitize_url(url):
    if validators.url(url):
        return urllib.parse.quote_plus(url)
    else:
        return None

def main():
    url = input("Enter the URL to sanitize: ")
    sanitized_url = sanitize_url(url)
    if sanitized_url is not None:
        print("Sanitized URL: ", sanitized_url)
    else:
        print("Invalid URL")

if __name__ == "__main__":
    main()