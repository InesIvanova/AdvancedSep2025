from collections import deque

queue = deque(input().split())
n_rotations = int(input()) - 1

while len(queue) > 1:
    queue.rotate(-n_rotations)
    name = queue.popleft()
    print(f"Removed {name }")

print(f"Last is {queue[0]}")
