#!/usr/bin/env python3
import sys
from functions import parse_filename
from functions import execute_commands
from functions import check_command_conflicts
from functions import find_th_files, select_file

def main():
    th_files = find_th_files()
    if not th_files:
        print("No .th files found in the current directory or subdirectories.")
        sys.exit(1)

    if len(th_files) == 1:
        chosen_file = th_files[0]
    else:
        chosen_file = select_file(th_files)

    try:
        text, commands = parse_filename(chosen_file)
        check_command_conflicts(commands)
        result = execute_commands(text, commands)
        if any(cmd.lower() == "output" for cmd in commands):
            print(f"{result.strip()}")
    except Exception as e:
        print(f"Error in file {chosen_file}: {e}")

if __name__ == "__main__":
    main()
