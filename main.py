import os

from constants import path_to_dir

path = os.path.join(path_to_dir, "06_file_handling", "nested", "nested_2", "to_delete.txt")

if os.path.exists(path):
    os.remove(path)

# try:
#     os.remove(path)
# except FileNotFoundError:
#     print("file does not exist")