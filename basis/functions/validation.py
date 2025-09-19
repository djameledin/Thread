import os, fnmatch

def find_th_files(root='..'):
    th_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        for filename in fnmatch.filter(filenames, "*.th"):
            th_files.append(os.path.join(dirpath, filename))
    return th_files

def select_file(files):
    print("Multiple .th files found:")
    for i, f in enumerate(files, 1):
        print(f"{i}) {f}")
    while True:
        choice = input("Choose file number: ").strip()
        if choice.isdigit():
            idx = int(choice)
            if 1 <= idx <= len(files):
                os.system('clear')
                return files[idx - 1]
        print("Invalid choice, Try again.")
