def squares(end):
    num = 1
    while num <= end:
        yield num * num
        num += 1

for el in squares(5):
    print(el)

print(list(squares(5)))