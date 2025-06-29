import os

path = os.path.join("..", "..", "..", "..", "files", "my_file.txt")

file = open(path)

print(file.read())