text = input()

try:
    times = int(input())
except BaseException:
    print('Variable times must be an integer')
else:
    print(text * times)

