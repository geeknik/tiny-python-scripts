import requests
import json

def search_data(platform, query):
    base_url = f"https://www.{platform}.com/"
    search_url = f"{base_url}search?q={query}"
    response = requests.get(search_url)
    return response.text

def save_data(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f)

def load_data(filename):
    with open(filename, 'r') as f:
        return json.load(f)

if __name__ == "__main__":
    platform = input("Enter the social media platform: ")
    query = input("Enter the search query: ")
    data = search_data(platform, query)
    save_data(data, 'search_results.json')
    print("Search results saved in 'search_results.json'")
