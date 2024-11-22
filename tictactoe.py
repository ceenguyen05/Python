"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = sum(row.count(X) for row in board) # count X on the board
    o_count = sum(row.count(O) for row in board) # count O on the board

    # game starts with X going first
    if x_count == o_count :
        return X
    else :
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    return {(i, j) for i in range(3) for j in range(3) if board[i][j] == EMPTY}

def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action
    # Check if the action is out of bounds
    if not (0 <= i < 3 and 0 <= j < 3):
        raise ValueError("Invalid action: cell is out of bounds")

    # Check if the cell is already occupied
    if board[i][j] is not EMPTY:
        raise ValueError("Invalid action: cell is not empty")

    # Create a deep copy of the board to avoid modifying the original board
    new_board = [row[:] for row in board]
    new_board[i][j] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != EMPTY:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != EMPTY:
            return board[0][i]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != EMPTY:
        return board[0][2]

    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    return winner(board) is not None or all(cell is not EMPTY for row in board for cell in row)

def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    winning_player = winner(board)
    if winning_player == X:
        return 1
    elif winning_player == O:
        return -1
    else:
        return 0

def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    def max_value(board):
        if terminal(board):
            return utility(board), None
        v = -math.inf
        best_action = None
        for action in actions(board):
            min_result, _ = min_value(result(board, action))
            if min_result > v:
                v = min_result
                best_action = action
        return v, best_action

    def min_value(board):
        if terminal(board):
            return utility(board), None
        v = math.inf
        best_action = None
        for action in actions(board):
            max_result, _ = max_value(result(board, action))
            if max_result < v:
                v = max_result
                best_action = action
        return v, best_action

    # Determine the optimal action based on the current player
    current_player = player(board)
    if current_player == X:
        _, action = max_value(board)
    else:
        _, action = min_value(board)
    return action

