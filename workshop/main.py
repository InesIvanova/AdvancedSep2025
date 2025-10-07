def check_row_winner(board, current_sign):
    for row in board:
        if row.count(current_sign) == 3:
            return True
    return False

def check_col_winner(board, current_sign):
    for col_index in range(3):
        count = 0
        for row_index in range(3):
            if board[row_index][col_index] == current_sign:
                count += 1
        if count == 3:
            return True
    return False

def check_diagonal_winner(board, current_sign):
    # primary diagonal
    count_primary = 0
    count_secondary = 0
    for index in range(3):
        if board[index][index] == current_sign:
            count_primary += 1
        if board[index][3 - index - 1] == current_sign:
            count_secondary += 1

    if count_primary == 3 or count_secondary == 3:
        return True
    return False


def check_for_winner(board, current_sign):
    if check_row_winner(board, current_sign) or  check_col_winner(board, current_sign) or check_diagonal_winner(board, current_sign):
        return True
    return False



def print_board(board):
    for row in board:
        print(f"| {' | '.join(row)} |")


board = [[" ", " ", " "] for _ in range(3)]
mapper = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2),
}
player_1_name = input("Player one name: ")
player_2_name = input("Player two name: ")
player_1_sign = input(f"{player_1_name} would you like to play with 'X' or 'O'? ").upper()

while player_1_sign not in ["X", "O"]:
    print("Please enter either 'X' or 'O'.")
    player_1_sign = input(f"{player_1_name} would you like to play with 'X' or 'O'? ").upper()

player_2_sign = 'O' if player_1_sign == 'X' else 'X'

print("This is the numeration of the board:")
print("| 1 | 2 | 3 |")
print("| 4 | 5 | 6 |")
print("| 7 | 8 | 9 |")

print(f"{player_1_name} starts first!")

turn = 1

while turn < 10:
    current_player =  player_1_name if turn % 2 != 0 else player_2_name
    current_sign = player_1_sign if turn % 2 != 0 else player_2_sign

    try:
        position = int(input(f"{current_player} please choose a free position between [1-9]: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if not (1 <= position <= 9):
        print("Please enter a valid number, between 1 and 9.")
        continue

    row,col = mapper[position]
    if board[row][col] != " ":
        print("This position is already occupied.")
        continue

    board[row][col] = current_sign
    print_board(board)

    if turn >= 5 and check_for_winner(board, current_sign):
        print(f"Congrats! {current_player} wins!")
        break

    turn += 1
else:
    print("Thanks for playing, no winner today!")
