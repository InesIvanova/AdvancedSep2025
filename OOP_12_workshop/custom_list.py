from copy import deepcopy
from sys import maxsize

class CustomList:
    def __init__(self, *args):
        self.__data = list(args)

    def append(self, el):
        self.__data.append(el)
        return self.__data

    def get_elements(self):
        return self.__data

    def remove(self, index):
        return self.__data.pop(index)

    def get(self, index):
        return self.__data[index]


    def extend(self, iterable):
        self.__data.extend(iterable)
        return self.__data

    def insert(self, index, el):
        self.__data.insert(index, el)
        return self.__data

    def pop(self):
        return self.__data.pop()

    def clear(self):
        self.__data.clear()

    def index(self, el):
        return self.__data.index(el)

    def count(self, el):
        return self.__data.count(el)

    def reverse(self):
        return list(reversed(self.__data))

    def copy(self):
        return deepcopy(self.__data)

    def size(self):
        return len(self.__data)

    def add_first(self, el):
        self.__data.insert(0, el)

    def dictionize(self):
        result = {}

        for index in range(0, len(self.__data), 2):
            try:
                result[self.__data[index]] = self.__data[index + 1]
            except IndexError:
                result[self.__data[index]] = " "

        return result

    def move(self, count):
        first_part = self.__data[:count]
        second_part = self.__data[count:]
        return second_part + first_part

    def sum(self):
        result = 0

        for el in self.__data:
            if isinstance(el, int) or isinstance(el, float):
                result += el
            else:
                result += len(el)

        return result

    def overbound(self):
        max_el = -maxsize
        biggest_el_index = None

        for index in range(0, len(self.__data)):
            if isinstance(self.__data[index], int) or isinstance(self.__data[index], float):
                element = self.__data[index]
            else:
                element = len(self.__data[index])

            if element > max_el:
                max_el = element
                biggest_el_index = index

        return biggest_el_index

    def underbound(self):
        min_el = maxsize
        min_el_index = None

        for index in range(0, len(self.__data)):
            if isinstance(self.__data[index], int) or isinstance(self.__data[index], float):
                element = self.__data[index]
            else:
                element = len(self.__data[index])

            if element < min_el:
                min_el = element
                min_el_index = index

        return min_el_index

