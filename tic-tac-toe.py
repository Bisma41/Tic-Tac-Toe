def initialize_board():
    return [['-', '-', '-'], ['-', '-', '-'], ['-', '-', '-']]

def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

def check_win(board):
    # Check rows
    for r in board:
        if r[0] == r[1] == r[2] != '-':
            return True
    # Check columns
    for c in range(3):
        if board[0][c] == board[1][c] == board[2][c] != '-':
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '-':
        return True
    if board[0][2] == board[1][1] == board[2][0] != '-':
        return True
    return False

def check_draw(board):
    for row in board:
        if '-' in row:
            return False
    return True

board = initialize_board()
current_player = 'A'

while True:
    print_board(board)

    valid_input = False
    while not valid_input:
        r = int(input("Enter row (0-2): "))
        c = int(input("Enter column (0-2): "))
        if r in range(3) and c in range(3) and board[r][c] == '-':
            valid_input = True
        else:
            print("Invalid input. Try again.")

    board[r][c] = current_player
    if check_win(board):
        print_board(board)
        print(f"Player {current_player} wins!")
        break
    elif check_draw(board):
        print_board(board)
        print("It's a draw!")
        break

    current_player = 'B' if current_player == 'A' else 'A'
