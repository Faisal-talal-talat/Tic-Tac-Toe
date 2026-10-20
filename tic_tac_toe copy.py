#"""A simple two-player Tic Tac Toe game for the terminal."""


WINNING_LINES = (
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
)


def print_board(board):
    """Display the board using cell numbers for empty spaces."""
    cells = [mark if mark != " " else str(index + 1) for index, mark in enumerate(board)]
    print()
    print(f" {cells[0]} | {cells[1]} | {cells[2]} ")
    print("---+---+---")
    print(f" {cells[3]} | {cells[4]} | {cells[5]} ")
    print("---+---+---")
    print(f" {cells[6]} | {cells[7]} | {cells[8]} ")
    print()


def find_winner(board):
    """Return the winning player mark, or None if nobody has won yet."""
    for first, second, third in WINNING_LINES:
        if board[first] != " " and board[first] == board[second] == board[third]:
            return board[first]
    return None


def board_is_full(board):
    return all(cell != " " for cell in board)


def get_move(board, player):
    while True:
        choice = input(f"Player {player}, choose a square (1-9): ").strip()

        if not choice.isdigit():
            print("Please enter a number from 1 to 9.")
            continue

        position = int(choice) - 1
        if position < 0 or position > 8:
            print("That square is outside the board. Pick 1 through 9.")
            continue

        if board[position] != " ":
            print("That square is already taken. Try another one.")
            continue

        return position


def play_round():
    board = [" "] * 9
    current_player = "X"

    print("Tic Tac Toe")
    print("Enter the number of an empty square to place your mark.")

    while True:
        print_board(board)
        move = get_move(board, current_player)
        board[move] = current_player

        winner = find_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins!")
            return

        if board_is_full(board):
            print_board(board)
            print("It's a draw!")
            return

        current_player = "O" if current_player == "X" else "X"


def main():
    while True:
        play_round()
        again = input("Play again? (y/n): ").strip().lower()
        if again not in ("y", "yes"):
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()

print("rfdvevcfdcefdcedfc")
print("frevrewvrv")