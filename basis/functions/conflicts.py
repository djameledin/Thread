def check_command_conflicts(commands: list):
    cmds = [c.lower() for c in commands]

    for cmd in cmds:
        if cmd in ["upper", "lower", "random"] and any(ch.isdigit() for ch in cmd):
            raise ValueError(f"Command '{cmd}' cannot contain numbers")

    if "upper" in cmds and "lower" in cmds:
        raise ValueError("Cannot use UPPER and lower together")

    if "random" in cmds and ("upper" in cmds or "lower" in cmds):
        raise ValueError("Cannot use random with UPPER or lower")
