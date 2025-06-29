import os
from constants import path_to_dir


path = os.path.join(path_to_dir, "files", "my_file.txt")
print(path)
file = open(path)
# print(file.name)
# print(file.mode)
# print(file.closed)
print(file.read())

