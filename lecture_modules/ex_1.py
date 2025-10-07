import math

number = int(input())

try:
    base = int(input())
    print(f"{math.log(number, base):.2f}")
except ValueError:
    print(f"{math.log(number):.2f}")