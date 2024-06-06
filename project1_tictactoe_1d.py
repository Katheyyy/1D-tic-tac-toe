
import random
print('Welcome to Tic Tac Toe - 1d: Have fun with the game. This is the initial board with 20 positions.\n You can place your x between position 0 - 19.')
def evaluate(board):
    if 'xxx' in board:
        return 'Congratulations, you won!'
    if 'ooo' in board:
        return 'Computer wins.'
    if '-' not in board:
        return 'Board is full, try a new game.'
    return '-'

def move(board, position, mark):
    # Is position inside the board?
    if position < 0 or position >= len(board):
        return "Error: Position is outside the board. Please only use numbers between 0 - 19."
    # Ensure mark is either 'x' or 'o'
    if mark not in ['x', 'o']:
        return "Error: Mark must be 'x' or 'o'"
    # Check if the position is already taken
    if board[position] in ['x', 'o']:
        return "Error: Position already taken. Choose another position."
    # Update the board
    updated_board = board[:position] + mark + board[position + 1:]
    return updated_board

def player_move(board, player_mark = 'x'):
    while True:
            position = int(input('Enter the position(0-19) you want to place your mark:'))
            # Check if the position is within the valid range
            if position < 0 or position >= len(board):
                print("Error: Position is outside the board. Please only use numbers between 0 - 19.")
                continue
            # Check if the position is already taken
            elif board[position] in ['x', 'o']:
                return "Error: Position already taken. Choose another position."
                continue
            # Update board with the player's move
            updated_game_board = board[:position] + player_mark + board[position + 1:]
            return updated_game_board

def pc_move(board, pc_mark = 'o'):
    while True:
            pc_position = random.randrange(0, 19)
            # Check if the position is already taken
            if board[pc_position] is '-':
                # Update the game board with the player's move
                updated_game_board = board[:pc_position] + pc_mark + board[pc_position + 1:]
                return updated_game_board

def tictactoe_1d():
    board = '-' * 20
    while True:
        board = player_move(board)
        print("Player's move:")
        print(board)
            # Check if the player has won or if the game is a draw
        result = evaluate(board)
        if 'xxx' in board:
            print('Congratulations, you won!') 
            break
        elif result == 'draw':
            print("It's a draw!")
            break
        board = pc_move(board)
        print("Computer's move:")
        print(board)
        result = evaluate(board)
        if result == 'ooo':
            print("Computer wins!")
            break
        elif result == 'draw':
            print("It's a draw!")
            break

tictactoe_1d()