rows, cols = [int(el) for el in input().split(", ")]

matrix = []

for _ in range(rows):
    data = [int(el) for el in input().split(", ")]
    matrix.append(data)


max_sum = float("-inf")
sub_matrix = []

for row_index in range(rows-1):
    for col_index in range(cols-1):
        current = matrix[row_index][col_index]
        next_element = matrix[row_index][col_index + 1]
        element_below = matrix[row_index + 1][col_index]
        element_diagonal = matrix[row_index + 1][col_index + 1]

        sum_elements = current + next_element + element_below + element_diagonal
        if sum_elements > max_sum:
            max_sum = sum_elements
            sub_matrix = [
                [current, next_element],
                [element_below, element_diagonal]
            ]

print(*sub_matrix[0])
print(*sub_matrix[1])
print(max_sum)