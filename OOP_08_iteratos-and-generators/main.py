my_list = [1, 3, 6, 10]

print([x**2 for x in my_list])


def square(iterable):
    index = 0
    while index < len(iterable):
        yield iterable[index]**2
        index += 1

print(list(square(my_list)))
print(list((x**2 for x in my_list)))
