import re
from pathlib import Path
from questionary import Choice, checkbox, confirm

# Paths
PROGRAM_DIR     = Path(__file__).parent
VSCODE_DIR      = PROGRAM_DIR.parent
OUT_PATH        = VSCODE_DIR    / "settings.json"
TEMPLATE_PATH   = VSCODE_DIR    / "settings.jstemp"
CACHE_PATH      = PROGRAM_DIR   / "cache"
# Regex
TEMPLATE_REGEX  = r'.*\/\/.*'
KEY_REGEX       = r'\$\{.+?\}'
# Lambda
KEY_EXTRACT     = lambda x: x[2:-1]

def replace_key(key, value, data):
    return data.replace("${%s}" % key, str(value).lower())

def get_template():
    with open(TEMPLATE_PATH) as data:
        template = data.read()

        # Remove comments
        template = re.sub(TEMPLATE_REGEX, '', template)

        # Remove empty lines
        template = '\n'.join([line for line in template.split('\n') if line.strip()])

        return template

def get_cache():
    try:
        with open(CACHE_PATH) as data:
            cache = set(data.read().split("\n"))
    except FileNotFoundError:
        cache = set()
    finally:
        return cache

def get_keys():
    with open(TEMPLATE_PATH) as data:
        template = data.read()
        keys = set(re.findall(KEY_REGEX, template))
        return keys

def get_choices(keys, cache):
    key_choices = []
    for item in map(KEY_EXTRACT, keys):
        selected = item in cache
        key_choices.append(Choice(item, checked=selected))
    return key_choices

def main():
    keys    = get_keys()
    cache   = get_cache()
    choices = get_choices(keys, cache)

    selected = set(
        checkbox(
            'Select which items to hide',
            choices=choices
        ).ask()
    )

    template = get_template()

    for item in keys:
        template = replace_key(item, item in selected, template)

    print(template)

    if confirm("Is this ok?").ask():
        with open(OUT_PATH, 'w+') as file:
            file.write(template)
    else:
        print("Aborted, nothing was written")

if __name__ == '__main__':
    main()