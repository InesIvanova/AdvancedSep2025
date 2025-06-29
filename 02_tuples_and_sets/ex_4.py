n = int(input())
parking = set()

for _ in range(n):
    direction, number = input().split(", ")
    if direction == "IN":
        parking.add(number)
    elif direction == "OUT":
        if number in parking:
            parking.remove(number)


if not parking:
    print("Parking Lot is Empty")
else:
    for car in parking:
        print(car)
