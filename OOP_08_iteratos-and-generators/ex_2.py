class reverse_iter:
    def __init__(self, iterable):
        self.iterable = iterable
        self.current = len(iterable)

    # def __iter__(self):
    #     return reversed(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        self.current -= 1
        if self.current >= 0:
            return self.iterable[self.current]
        else:
            raise StopIteration


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)


for el in reversed([100, 200, 300]):
    print(el)