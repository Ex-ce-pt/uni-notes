import os
from pprint import pprint

def get_all_files(path: str) -> list[str]:
    return [os.path.join(dirpath, filename)
            for dirpath, dirnames, filenames in os.walk(path)
            for filename in filenames
            if filename.endswith('.md')]


def process_file(filepath: str):
    content = ''
    with open(filepath, 'r') as file:
        content = file.read()

    content = content.replace(' /w ', ' w/ ').replace('Explanation', 'Comment')

    with open(filepath, 'w') as file:
        file.write(content)

def main():
    for f in get_all_files('./Foundations of Chemistry/'):
        process_file(f)

main()

# Something happened to the Acids & Bases note

