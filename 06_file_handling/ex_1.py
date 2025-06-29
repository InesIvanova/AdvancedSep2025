import os.path

from constants import path_to_dir

path = os.path.join(path_to_dir, "files", "text.txt")

try:
    file = open(path)
    print("file found")
    print(file.read())
    file.close()
except FileNotFoundError:
    print("file not found")
