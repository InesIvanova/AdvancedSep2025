from collections import deque
liters = int(input())

name = input()


queue = deque()
while name != "Start":
    queue.append(name)
    name = input()


data = input()

while data != "End":
    if data.startswith("refill"):
        liters_to_fill = int(data.split()[-1])
        liters += liters_to_fill
    elif data.isdigit():
        name = queue.popleft()
        liters_wanted = int(data)
        if liters_wanted <= liters:
            liters -= liters_wanted
            print(f"{name} got water")
        else:
            print(f"{name} must wait")
    data = input()

print(f"{liters} liters left")

