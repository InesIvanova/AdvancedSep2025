def is_in_range(param, scope):
    if 0 <= param < scope:
        return True
    return False

direction_mapper = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}

rows, cols = [int(el) for el in input().split(", ")]


current_position = None
bomb_position = None
matrix = []
for index in range(rows):
    data = list(input())
    if "C" in data:
        current_position = (index, data.index("C"))
    if "B" in data:
        bomb_position = (index, data.index("B"))
    matrix.append(data)


seconds = 16


while True:
    if seconds <= 0:
        # Out of time
        print(f"Terrorists win!\nBomb was not defused successfully!\nTime needed: {abs(seconds)} second/s.")
        break

    direction = input()

    current_row = current_position[0]
    current_col = current_position[1]
    if direction == "defuse":
        if current_position != bomb_position:
            seconds -= 2
            continue
        else:
            seconds -= 4
            if seconds >= 0:
                matrix[current_row][current_col] = "D"
                print(f"Counter-terrorist wins!\nBomb has been defused: {seconds} second/s remaining.")
                break
            else:
                matrix[current_row][current_col] = "X"
                print(f"Terrorists win!\nBomb was not defused successfully!\nTime needed: {abs(seconds)} second/s.")
                break


    seconds -= 1
    row_movement, col_movement = direction_mapper[direction]
    next_row = current_row + row_movement
    next_col = current_col + col_movement
    # Option 2 (replaces 53-55)
    # cur_pos = list(map(lambda x, y: x + y, current_position, direction_mapper[direction]))


    if not is_in_range(next_row, rows) or not is_in_range(next_col, cols):
        continue

    current_position = (next_row, next_col)

    if matrix[current_position[0]][current_position[1]] == "T":
        # Both are killed
        matrix[current_position[0]][current_position[1]] = "*"
        print("Terrorists win!")
        break


for row in matrix:
    print(*row, sep='')
    # print(''.join(row))

