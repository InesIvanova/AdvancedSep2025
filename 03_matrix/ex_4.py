n_rows, n_cols  = [int(el) for el in input().split(", ")]

matrix = []

for i in range(n_rows):
    data = [int(el) for el in input().split()]
    matrix.append(data)


for col_index in range(n_cols):
    col_sum = 0
    for row_index in range(n_rows):
        col_sum += matrix[row_index][col_index]
    print(col_sum)
