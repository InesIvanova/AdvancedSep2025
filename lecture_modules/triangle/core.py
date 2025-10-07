def print_upper_part(n):
    for row in range(1, n+1):
        for num in range(1, row+1):
            print(num, end=' ')
        print()


def print_bottom_part(n):
    for row in range(1, n):
        for num in range(1, n-row+1):
            print(num, end=' ')
        print()


def print_triangle(n):
    print_upper_part(n)
    print_bottom_part(n)