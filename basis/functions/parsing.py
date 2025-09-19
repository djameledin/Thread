import os, re

def parse_filename(filename: str):
    basename = os.path.splitext(os.path.basename(filename))[0]
    match = re.fullmatch(r'return\(type\["([^"]+)"\](?:,\s*([^)]+))?\)', basename)
    if not match:
        raise ValueError('Filename must match return(type["text"][,commands]) format')
    text = match.group(1)
    commands = [cmd.strip() for cmd in match.group(2).split('.') if match.group(2)] if match.group(2) else []
    return text, commands
