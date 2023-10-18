import random

def create_board(height, width, default_char='-'):
    # Membuat board dengan list comprehension
    board = [[default_char for _ in range(width)] for _ in range(height)]
    return board

generate_random_position = lambda height, width: (random.randint(0, height - 1), random.randint(0, width - 1))

def place_piece(board, row, col, piece_char):
    # Menempatkan bidak pada posisi yang ditentukan
    if 0 <= row < len(board) and 0 <= col < len(board[0]):
        board[row][col] = piece_char
    else:
        print("Posisi di luar batas board.")

def print_board(board):
    for row in board:
        print(' ').join(row)

def move_piece(board, position, move_direction):
    # Memindahkan bidak ke arah yang ditentukan
    row, col = position
    new_row, new_col = row, col

    if move_direction == 'w' and row > 0 and board[row - 1][col] != '#':
        new_row = row - 1
    elif move_direction == 's' and row < len(board) - 1 and board[row + 1][col] != '#':
        new_row = row + 1
    elif move_direction == 'a' and col > 0 and board[row][col - 1] != '#':
        new_col = col - 1
    elif move_direction == 'd' and col < len(board[0]) - 1 and board[row][col + 1] != '#':
        new_col = col + 1

    if (new_row, new_col) != (row, col):
        board[row][col], board[new_row][new_col] = board[new_row][new_col], board[row][col]
        return new_row, new_col
    else:
        return row, col

def main():
    # Input panjang dan lebar dari pengguna
    height = int(input("Masukkan panjang board: "))
    width = int(input("Masukkan lebar board: "))

    board = create_board(height, width)

    position_generator = generate_random_position(height, width)
    start_row, start_col = next(position_generator)
    goal_row, goal_col = next(position_generator)

    # Menempatkan bidak (simbol 'A') pada posisi awal yang dihasilkan secara acak
    place_piece(board, start_row, start_col, 'A')
    place_piece(board, goal_row, goal_col, 'O')

    print("Selamat datang dalam permainan!")
    print_board(board)

    while True:
        move_direction = input("Masukkan arah pergerakan (w/a/s/d) atau 'q' untuk keluar: ").lower()

        if move_direction == 'q':
            print("Anda keluar dari permainan.")
            break

        if move_direction not in ['w', 'a', 's', 'd']:
            print("Arah pergerakan tidak valid. Harap masukkan arah yang benar.")
            continue

        start_row, start_col = move_piece(board, (start_row, start_col), move_direction)
        print_board(board)

        if (start_row, start_col) == (goal_row, goal_col):
            print("Selamat! Anda menang!")
            break

if __name__ == "__main__":
    main()
