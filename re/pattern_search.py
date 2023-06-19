
import re

def pattern_search(pattern, file_path):
    with open(file_path, 'r') as file:
        content = file.read()
        matches = re.findall(pattern, content)
        return matches

if __name__ == "__main__":
    pattern = input("Enter the pattern to search: ")
    file_path = input("Enter the file path: ")
    matches = pattern_search(pattern, file_path)
    print(f"Found {len(matches)} matches.")
    for match in matches:
        print(match)
