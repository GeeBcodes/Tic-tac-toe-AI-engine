
def print_board(board):
    """
    Displays the current Tic-Tac-Toe board in a 3x3 grid format.
    board is a list of length 9, where each element is ' ', 'X', or 'O'.
    Indices:
      0 | 1 | 2
     ---+---+---
      3 | 4 | 5
     ---+---+---
      6 | 7 | 8
    """
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")

def check_winner(board):
    """
    Checks if there's a winner on the board.
    Returns 'X' if X wins, 'O' if O wins, or None if there is no winner yet.
    """
    winning_lines = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    
    for (a, b, c) in winning_lines:
        if board[a] != " " and board[a] == board[b] == board[c]:
            return board[a]  # 'X' or 'O'
    
    return None

def is_board_full(board):
    """
    Returns True if there are no empty spaces left on the board.
    Otherwise, returns False.
    """
    return " " not in board

def make_ai_move(board):
    """
    Makes a move for AI (X) based on the following priority rules:
    1) Win if possible.
    2) Block opponent’s (O) winning move.
    3) Take center if available.
    4) Take any corner if available.
    5) Take any side if available.
    
    This function directly modifies the board list.
    """
    # Define winning lines once for convenience:
    winning_lines = [
        (0,1,2), (3,4,5), (6,7,8),  # rows
        (0,3,6), (1,4,7), (2,5,8),  # columns
        (0,4,8), (2,4,6)            # diagonals
    ]
    
    # RULE 1: Win if possible
    # If there's a line with 2 X's and 1 empty space, place X in that empty space.
    for (a, b, c) in winning_lines:
        if board[a] == board[b] == "X" and board[c] == " ":
            board[c] = "X"
            return
        if board[a] == board[c] == "X" and board[b] == " ":
            board[b] = "X"
            return
        if board[b] == board[c] == "X" and board[a] == " ":
            board[a] = "X"
            return
    
    # RULE 2: Block opponent’s (O) win
    # If there's a line with 2 O's and 1 empty space, place X in that empty space.
    for (a, b, c) in winning_lines:
        if board[a] == board[b] == "O" and board[c] == " ":
            board[c] = "X"
            return
        if board[a] == board[c] == "O" and board[b] == " ":
            board[b] = "X"
            return
        if board[b] == board[c] == "O" and board[a] == " ":
            board[a] = "X"
            return
    
    # RULE 3: Take the center if available
    if board[4] == " ":
        board[4] = "X"
        return
    
    # RULE 4: Take any corner if available
    corners = [0, 2, 6, 8]
    for corner in corners:
        if board[corner] == " ":
            board[corner] = "X"
            return
    
    # RULE 5: Take any side if available
    sides = [1, 3, 5, 7]
    for side in sides:
        if board[side] == " ":
            board[side] = "X"
            return

def main():
    """
    Main function that runs the rule-based Tic-Tac-Toe game:
      - Human is 'O'
      - AI is 'X'
    The game continues until one player wins or the board is full.
    """
    # Create an empty board
    board = [" "] * 9
    current_player = "O"  # Let the user (O) go first
    
    print("Welcome to Rule-Based Tic-Tac-Toe!")
    print("You are 'O' and the AI is 'X'.")
    print("Positions on the board are numbered 1 through 9:\n")
    
    # Show position references for user
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print("\nLet's begin!\n")
    
    # Game loop
    while True:
        print_board(board)
        winner = check_winner(board)
        
        # Check if we have a winner or a tie
        if winner is not None:
            print(f"\nGame Over! Winner is {winner}\n")
            break
        if is_board_full(board):
            print("\nGame Over! It's a tie!\n")
            break
        
        # If it's user's turn
        if current_player == "O":
            # Get user input (1-9) and convert to index (0-8)
            move = input("Enter your move (1-9): ")
            
            # Validate input
            if not move.isdigit():
                print("Invalid input. Please enter a number between 1 and 9.")
                continue
            move_index = int(move) - 1
            if move_index < 0 or move_index > 8:
                print("Invalid position. Must be 1 to 9.")
                continue
            if board[move_index] != " ":
                print("That position is already taken. Try again.")
                continue
            
            # Place user's move
            board[move_index] = "O"
            
            # Switch turn to AI
            current_player = "X"
        
        # If it's AI's turn
        else:
            print("\nAI (X) is making its move...\n")
            make_ai_move(board)
            current_player = "O"

    # Final board state
    print_board(board)
    print("Thank you for playing!")

if __name__ == "__main__":
    main()
