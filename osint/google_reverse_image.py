import requests
from PIL import Image
import io

def reverse_image_search(image_path):
    search_url = "https://www.google.com/searchbyimage/upload"
    multipart = {'encoded_image': (image_path, open(image_path, 'rb')), 'image_content': ''}
    response = requests.post(search_url, files=multipart, allow_redirects=False)
    fetch_url = response.headers['Location']

    return fetch_url

def save_image_from_url(url, save_path):
    response = requests.get(url)
    image = Image.open(io.BytesIO(response.content))
    image.save(save_path)

def main():
    image_path = "path_to_your_image.jpg"
    save_path = "path_to_save_image.jpg"
    fetch_url = reverse_image_search(image_path)
    save_image_from_url(fetch_url, save_path)

if __name__ == "__main__":
    main()
