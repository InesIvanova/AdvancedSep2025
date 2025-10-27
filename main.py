# def first_n(n):
#     num = 0
#     while num < n:
#         yield num
#         num += 1
#
# result = first_n(5)
# for el in result:
#     print(el)


def my_gen():
    n = 1
    yield n

    n += 1
    yield n

    n += 1
    yield n


result = my_gen()
for el in result:
    print(el)
