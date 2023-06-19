import os
import sys
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def handle_image(file_path):
    image = Image.open(file_path)
    exif_data = image._getexif()
    if exif_data is not None:
        for tag, value in exif_data.items():
            tag_name = TAGS.get(tag, tag)
            if isinstance(value, bytes):
                value = value.decode(errors="replace")
            print(f"{tag_name}: {value}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python forensic_image_analyzer.py [IMAGE_PATH]")
        sys.exit(1)

    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print(f"{file_path} does not exist.")
        sys.exit(1)

    handle_image(file_path)

if __name__ == "__main__":
    main()
