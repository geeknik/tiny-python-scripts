import os
from PIL import Image
from PIL.ExifTags import TAGS

def extract_metadata(file_path):
    image = Image.open(file_path)
    exifdata = image._getexif()
    if exifdata is not None:
        for tag_id in exifdata:
            tag = TAGS.get(tag_id, tag_id)
            data = exifdata.get(tag_id)
            if isinstance(data, bytes):
                data = data.decode(errors='replace')
            print(f"{tag:25}: {data}")

if __name__ == "__main__":
    file_path = input("Enter the path to the file: ")
    extract_metadata(file_path)
