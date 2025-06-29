import os

from constants import path_to_dir

path = os.path.join(path_to_dir, "files", "numbers.txt")

file = open(path)
# numbers = [int(el) for el in file.read().split("\n") if el]
total = 0
for line in file:
    total += int(line)

print(total)