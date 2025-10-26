def print_row(spaces, stars):
    print(f"{' ' * spaces}{'* ' * stars}")


def print_top(n):
    for row in range(1, n+1):
        print_row(n-row, row)


def print_bottom(n):
    for row in range(1, n):
        print_row(row, n-row)

def print_rhombus(n):
    print_top(n)
    print_bottom(n)


n = int(input())
print_rhombus(n)