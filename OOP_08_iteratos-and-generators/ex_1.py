class custom_range:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.current = start - 1


    def __iter__(self):
        return self

    def __next__(self):
        self.current += 1
        if self.current <= self.end:
            return self.current
        else:
            self.current = self.start - 1
            raise StopIteration


# Example how to do with generators
# def custom_range(start, end):
#     current = start
#     while current <= end:
#         yield current
#         current += 1
#
#
# a = [100, 200, 300]
# for el in a:
#     print(el)
#
# for el in a:
#     print(el)
#
#
# for el in a:
#     print(el)
#
# for el in a:
#     print(el)


one_to_ten = custom_range(1, 3)
for num in one_to_ten:
    print(num)

for num in one_to_ten:
    print(num)