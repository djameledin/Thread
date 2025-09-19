import re, random

def execute_commands(output: str, commands: list) -> str:
    actions = {
        "esrever": lambda s: s[::-1],
        "nvwls": lambda s: re.sub(r'[aeiouAEIOU]', '', s),
        "Capitalize": str.title,
        "words_reverse": lambda s: ' '.join(s.split()[::-1]),
        "snak_e": lambda s: '_'.join(s.split()),
        "shuflfe": lambda s: ' '.join(random.sample(s.split(), len(s.split()))),
        "rAndOm": lambda s: ''.join(c.upper() if random.choice([True, False]) else c.lower() for c in s),
        "UPPER": str.upper,
        "lower": str.lower,
    }

    for cmd in commands:
        if cmd.lower() == "output":
            continue
        if cmd not in actions:
            raise ValueError(f"Unknown command: {cmd}")
        output = actions[cmd](output)
    return output.replace('||', '\n') + '\n'
