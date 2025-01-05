import json
import toml
import re
from pathlib import Path

PROGRAM_DIR     = Path(__file__).parent.parent
OUT_PATH        = PROGRAM_DIR   / "settings.json"
CONFIG_DIR      = PROGRAM_DIR   / "config"
KEYS_PATH       = CONFIG_DIR    / "keys.toml"
TEMPLATE_PATH   = CONFIG_DIR    / "settings.jstemp"
REGEX           = r'.*\/\/.*'

def replace_placeholders(key, value, data):
    return data.replace("${%s}" % key, str(value).lower())

def main():
    with open(TEMPLATE_PATH) as data:
        template = data.read()

        # Remove comments
        template = re.sub(REGEX, '', template)

        # Remove empty lines
        template = '\n'.join([line for line in template.split('\n') if line.strip()])

    with open(KEYS_PATH) as data:
        settings = toml.load(data)

    for key, value in settings.items():
        template = replace_placeholders(key, value, template)

    with open(OUT_PATH, 'w+') as file:
        file.write(template)

if __name__ == '__main__':
    main()