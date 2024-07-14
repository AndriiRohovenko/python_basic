import sys
from pathlib import Path
from colorama import Fore

def is_file(item):
    return item.is_file()

def print_directory_structure(path, level=0):
    try:
        items = list(path.iterdir())
        items.sort(key=is_file)
        for item in items:
            if item.is_dir():
                print("  " * level + Fore.BLUE + f"{item.name}/")
                print_directory_structure(item, level + 1)
            else:
                print("  " * level + Fore.GREEN + f"{item.name}")
    except PermissionError:
        print("  " * level + Fore.RED + "Access Denied")

def main(directory):
    path = Path(directory)
    if path.exists() and path.is_dir():
        print_directory_structure(path)
    else:
        print(Fore.RED + "The provided path does not exist or is not a directory.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(Fore.RED + "Please Provide only one argument Dir Path!")
    else:
        main(sys.argv[1])
