import json
import toml
import re
from pathlib import Path

PROGRAM_DIR = Path(__file__).parent
CONFIG_DIR  = PROGRAM_DIR.parent / "config"
KEYS_PATH   = PROGRAM_DIR / "keys.toml"

def replace_placeholders(key, value, data):
    return data.replace("${%s}" % key, str(value).lower())

def main():
    with open(KEYS_PATH) as data:
        settings = toml.load(data)

    for file in TEMPLATE_DIR.walk():
        infile  = PROGRAM_DIR   / "templates"
        outfile = CONFIG_DIR    / "settings.json"

        with open(infile) as data:
            template = data.read()

            # Remove comments
            template = re.sub(r'.*\/\/.*', '', template)

            # Remove empty lines
            template = '\n'.join([line for line in template.split('\n') if line.strip()])

        for key, value in settings.items():
            template = replace_placeholders(key, value, template)

        with open(outfile, 'w+') as file:
            file.write(template)

if __name__ == '__main__':
    main()